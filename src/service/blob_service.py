import os
import streamlit as st
from utils.config import Config
from azure.storage.blob import BlobServiceClient

def upload_blob(uploaded_file, blob_name):
    try:
        storage_client = BlobServiceClient.from_connection_string(
            Config.AZURE_STORAGE_CONNECTION_STRING
        )
        
        client_blob = storage_client.get_blob_client(
            container=Config.CONTAINER_NAME,
            blob=blob_name
        )
        
        client_blob.upload_blob(uploaded_file, overwrite=True)
        
        return client_blob.url
    except Exception as error:
        st.error(f"Erro ao enviar o arquivo para o Blob Storage: {error}")
        return None
