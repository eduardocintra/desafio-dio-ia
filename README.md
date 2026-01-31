# Desafio: Reconhecimento de Documentos com Azure Document Intelligence

Este repositório apresenta uma solução desenvolvida para o desafio de implementação de serviços de IA voltados ao reconhecimento de documentos por meio do Azure Document Intelligence. A proposta do projeto é demonstrar como extrair informações estruturadas a partir de documentos não estruturados, como faturas, cartões de visita e formulários.

## 📋 Sobre o Projeto

O projeto utiliza o **Azure AI Document Intelligence** (anteriormente conhecido como Form Recognizer) para automatizar o processo de leitura e processamento de documentos. A tecnologia de **Machine Learning** é aplicada para identificar campos-chave, tabelas e textos em diversos formatos de arquivos.


### Funcionalidades:
- Extração de texto por meio de OCR.
- Análise da estrutura e do layout dos documentos.
- Uso de modelos pré-treinados (por exemplo: Invoices, Receipts).
- Organização dos dados extraídos no formato JSON.


## 🚀 Tecnologias Utilizadas

- **Microsoft Azure**: Plataforma de serviços em nuvem utilizada no projeto.
- **Azure AI Document Intelligence**: Serviço de IA responsável pela análise e extração de informações de documentos.
- **JSON**: Formato adotado para a representação dos dados estruturados.


## 🛠️ Passo a Passo da Implementação

1. **Criação do Recurso**: Um recurso do tipo *Document Intelligence* foi provisionado no portal do Azure.
2. **Configuração do Ambiente**: Uso do **Document Intelligence Studio** para realizar testes rápidos e visualizar as informações extraídas.
3. **Processamento dos Arquivos**: Envio de documentos de exemplo (disponíveis na pasta `inputs`) para análise.
4. **Extração dos Resultados**: Os resultados gerados (armazenados na pasta `outputs`) demonstram como a IA interpretou e estruturou os dados do documento original.


## 📁 Estrutura do Repositório

- `inputs/`: Armazena os documentos (PDFs e imagens) utilizados nos testes de reconhecimento.
- `outputs/`: Contém os arquivos JSON e/ou capturas de tela com os resultados gerados pelo serviço do Azure.
- `scripts/`: (Opcional) Scripts em Python ou comandos de linha de comando usados para integração.


## 📊 Exemplos de Resultados

Ao processar uma fatura, o modelo conseguiu identificar com precisão:
- Nome e endereço da empresa.
- Data de emissão do documento.
- Itens presentes na tabela de serviços ou produtos.
- Valores de taxas e o total da fatura.
