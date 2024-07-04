# Streamlit App

This is a helm adoption of a simple Hello Streamlit App built to run on Kubernetes, specifically on the KNative Serverless framework. The workloads are serverless and they shut down after limited usage, with the exception being the stateful workload of postgres. This Helm chart is not the same as the licensed Helm chart as labeled on the documentation.

## Warnings and Knonw issues

### Streamlit in k8s

We have seen that deploying Streamlit in k8s with **more than 1 replica** can make the application behave erratically (e.g [issue1](https://discuss.streamlit.io/t/loadbalancing-in-kubernetes-issues-cookie-help/39498) [issue2](https://discuss.streamlit.io/t/deploy-streamlit-using-kubernetes/60127)). To solve this you can implement Sticky Sessions, so the same isuer is always redirected to the same replica for the session duration, for more information on this check our [docs](https://hosted-apps-us.pwclabs.pwcglb.com/docs/developerguide/sticky_sessions/)

The Sicky Sessions will only work with a Deployment (as specified in our docs), for a POC application it might be better to keep using Knative with only 1 replica.

### Websockets in Knative

Streamlit uses websockets for all communications with the client, when it is deployed with Knative Services, the websocket gets reseted every 5 minutes (socket gets closed and a new one is open). This is ok for most of the applications, but depending your app and how you have coded it, it might cause some disruptions, for example if you have long running backend jobs (of more than 5 minutes) it can break the application flow. In case you are seeing issues with the application auto refreshing after around 5 minutes, we recommend deploying your application as a k8 Deployment instead of a Knative Service (as the deployment is a stateful resource you will need a valid apptioid).

## Streamlit Clean architecture example

A Clean Architecture Practice with Streamlit inbuilt

### Basic Folder Structure

> src/app/main.py

The major application declaration file.

> src/app

The Application Layer that defines the web application code. Update the Dockerfile and requirements.txt for all dependencies.

> src/test

Pytest unit testing implementation

### Dependencies

- `Streamlit`: Basic Web App Development
- `Azure Storage Blob`: Integrating with the Data Platform

### Data Platform Integration

The Streamlit Template integrates with Data Platform out of the box. The implemented functions can be found in src/app/shared/infrastructure/azureblobstorage/blob_storage_functions.py

The followin functions are available:
- list_files: returns a list of blobs associated to the Azure Blob Storage from the container associated with the ENGAGEMENT_ID
- download_blob: returns byte data of a specific blob - replace the first argument with a filename present in the container
- get_file_stats: returns json result of a blob's metadata - replace the first argument with a filename present in the container

### Run the project

> install dependencies on local environment

```bash
make lib-install
```

> On repo root folder, to execute over local docker container

```bash
make launch
```

> On repo root folder, to execute directly using streamlit run

```bash
make local-launch
```

### Test Driven Development

> install development dependencies on local environment

```bash
make dev-install
```

> to validate unit tests and code with TDD

```bash
make testme
```

### Code Lint

> run pylint

```bash
make lint
```

> apply aggressive linting over file src/x.py

```bash
make lintme f=src/x.py
```

> apply aggressive linting over file all python files

```bash
make lintall
```

### Documentation & Reference

- [Streamlit](https://streamlit.io/)