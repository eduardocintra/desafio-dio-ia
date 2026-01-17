# Translator Azure

Projeto em Python que extrai o texto de um artigo a partir de uma URL e traduz o conteúdo usando **Azure OpenAI**.

Este projeto foi criado com foco em simplicidade, servindo como exemplo prático de uso do Azure OpenAI para tradução de textos.

---

## Visão geral

O projeto realiza as seguintes etapas:

1. Acessa uma URL informada
2. Extrai apenas o texto da página (remove scripts e estilos)
3. Envia o texto para o Azure OpenAI
4. Retorna o conteúdo traduzido em formato **Markdown**

---

## Tecnologias utilizadas

- Python 3
- Azure OpenAI
- LangChain
- Requests
- BeautifulSoup
- Python Dotenv

---

## Pré-requisitos

Antes de começar, você precisa ter:

- **Python 3.9 ou superior**
- Conta no **Azure**
- Um recurso de **Azure OpenAI** criado
- Um **deployment** configurado (exemplo: `gpt-4o-mini`)
- Git (opcional, para clonar o repositório)

---
## Configurações
Crie um arquivo .env na raiz do projeto com as variáveis:

```bash
AZURE_ENDPOINT=https://seu-endpoint.openai.azure.com/
AZURE_API_KEY=sua-chave-da-api
```

---

## Uso

```bash
python .\main.py
```