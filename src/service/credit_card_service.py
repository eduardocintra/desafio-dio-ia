from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.config import Config

def analyze_credit_card(image_url):
    
    api_credential = AzureKeyCredential(Config.SUBSCRIPTION_KEY)

    doc_client = DocumentIntelligenceClient(
        Config.ENDPOINT,
        api_credential
    )

    analysis_operation = doc_client.begin_analyze_document(
        "prebuilt-creditCard",
        AnalyzeDocumentRequest(url_source=image_url)
    )

    analysis_result = analysis_operation.result()

    for analyzed_doc in analysis_result.documents:
        extracted_fields = analyzed_doc.get("fields", {})

        return {
            "card_name": extracted_fields.get("CardHolderName", {}).get("content"),
            "card_number": extracted_fields.get("CardNumber", {}).get("content"),
            "expiry_date": extracted_fields.get("ExpirationDate", {}).get("content"),
            "bank_name": extracted_fields.get("IssuingBank", {}).get("content")
        }
