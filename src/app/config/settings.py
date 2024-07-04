"""Global Settings holder for the Application"""

import os


class Settings:
    """Settings class"""
    PROJECT_NAME: str = "Streamlit App Template"
    PROJECT_VERSION: str = "1.0.0"
    DESCRIPTION: str = "Streamlit example from the GCaaS Team"

    ENGAGEMENT_ID: str = os.environ.get("ENGAGEMENT_ID", "")
    SECRETS_DIRECTORY: str = os.environ.get("SECRETS_DIRECTORY", "/var/secrets")

    try:
        with open(f"{SECRETS_DIRECTORY}/SAS_TOKEN", "r") as f:
            AZURE_BLOB_SAS_TOKEN: str = f.read().strip()
    except Exception:
        AZURE_BLOB_SAS_TOKEN: str = ""

    try:
        with open(f"{SECRETS_DIRECTORY}/STORAGE_ACCOUNT_NAME", "r") as f:
            STORAGE_ACCOUNT_NAME: str = f.read().strip()
    except Exception:
        STORAGE_ACCOUNT_NAME: str = ""


settings = Settings()
