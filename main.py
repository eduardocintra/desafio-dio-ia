import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from langchain_openai.chat_models.azure import AzureChatOpenAI


def fetch_article_content(page_url):
    response = requests.get(page_url)

    if response.status_code != 200:
        print("Erro ao acessar a URL")
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style"]):
        tag.decompose()

    raw_text = soup.get_text(separator=" ")
    lines = (line.strip() for line in raw_text.splitlines())
    parts = (segment.strip() for line in lines for segment in line.split("  "))

    cleaned_text = "\n".join(segment for segment in parts if segment)
    return cleaned_text


# Carrega variáveis do ambiente
load_dotenv()

chat_client = AzureChatOpenAI(''
    azure_endpoint=os.getenv("AZURE_ENDPOINT"),
    api_key=os.getenv("AZURE_API_KEY"),
    api_version="2026-01-17-0001",
    deployment_name="gpt-4o-mini",
    max_retries=0
)


def translate_text(content, target_language):
    prompt = [
        ("system", "Você é um assistente especializado em tradução de textos"),
        ("user", f"Traduza o texto a seguir para {target_language} e formate em markdown:\n\n{content}")
    ]

    result = chat_client.invoke(prompt)
    return result.content


if __name__ == "__main__":
    article_url = "https://sua-url.com/artigo"

    article_text = fetch_article_content(article_url)

    if article_text:
        translated_article = translate_text(article_text, "pt-br")
        print(translated_article)
