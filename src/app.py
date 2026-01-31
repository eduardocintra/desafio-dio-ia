import streamlit as st
from service.blob_service import upload_blob
from service.credit_card_service import analyze_credit_card


def setup_ui():
    st.title("Upload de Arquivo DIO - Desafio 1 - Azure - Fake Docs")
    selected_file = st.file_uploader(
        "Selecione uma imagem",
        type=["png", "jpg", "jpeg"]
    )

    if selected_file:
        original_name = selected_file.name

        # Upload do arquivo para o Azure Blob Storage
        uploaded_url = upload_blob(selected_file, original_name)

        if uploaded_url:
            st.success(f"Arquivo {original_name} enviado com sucesso!")
            card_data = analyze_credit_card(uploaded_url)
            render_image_and_result(uploaded_url, card_data)
        else:
            st.error(f"Erro ao enviar o arquivo {original_name}.")


def render_image_and_result(image_url, card_data):
    st.image(image_url, caption="Imagem enviada", width=500)
    st.write("Resultado da validação:")

    if card_data and (card_data.get("card_number") or card_data.get("card_name")):
        st.markdown(
            "<h1 style='color:green;'>Cartão Válido</h1>",
            unsafe_allow_html=True
        )
        st.write(f"Nome do Titular: {card_data.get('card_name')}")
        st.write(f"Banco Emissor: {card_data.get('bank_name')}")
        st.write(f"Data de Validade: {card_data.get('expiry_date')}")
    else:
        st.markdown(
            "<h1 style='color:red;'>Cartão Inválido</h1>",
            unsafe_allow_html=True
        )
        st.write("Este não é um cartão de crédito válido.")


if __name__ == "__main__":
    setup_ui()
