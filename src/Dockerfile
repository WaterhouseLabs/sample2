###############################
#      APP IMG              #
###############################
FROM python:3.12-slim

WORKDIR /streamlit-app

COPY ./app ./app
COPY Pipfile .
COPY Pipfile.lock .

# Add PwC Certificates
COPY certs/pwc.crt /usr/local/share/ca-certificates/pwc.crt
RUN update-ca-certificates
ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN addgroup --gid 1000 appuser && \
    adduser --disabled-password --uid 1000 --ingroup appuser --comment "" --shell /bin/bash appuser && \
    chown -R appuser:appuser /streamlit-app && \
    chown -R appuser:appuser /home/appuser

USER appuser

# Dependencies install
RUN python3 -m pip install pipenv && \
    python3 -m pipenv sync

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

CMD ["python3", "-m", "pipenv", "run", "streamlit", "run", "app/main.py", "--server.address", "0.0.0.0", "--server.port", "8080"]