import logging
from azure.storage.blob import BlobServiceClient


logger = logging.getLogger(__name__)


class AzureBlobStorageService:
    def __init__(self, storage_account: str, sas_token: str, engagement_id: str):
        self.storage_account = storage_account
        self.sas_token = sas_token
        self.engagement_id = engagement_id

        self.client = BlobServiceClient(f"https://{self.storage_account}.blob.core.windows.net", self.sas_token)
        self.container_client = self.client.get_container_client(engagement_id)

    def get_blob_list(self) -> list[dict]:
        try:
            blob_list = self.container_client.list_blobs()
            return [file for file in blob_list]
        except Exception as ex:
            logger.error(f"There was an error obtaining the list of files from BlobStorage. Error is {ex}")
            return ex
