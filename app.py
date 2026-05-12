import os
import streamlit as st

from aes_crypto import run_aes_demo
from rsa_crypto import run_rsa_demo

st.set_page_config(page_title="Crypto Demo (AES vs RSA)", page_icon="🔐", layout="wide")

st.title("🔐 Криптография демосу: AES vs RSA")
st.write("Бул колдонмо бир эле текстти AES жана RSA менен шифрлеп, жыйынтыгын салыштырып берет.")

message = st.text_area(
    "Шифрлене турган текст",
    value="Блокчейн транзакциясынын купуя маалыматтары. 100 BTC которулду.",
    height=120,
)

work_dir = st.text_input("AES файл сакталуучу папка", value=os.path.join(os.getcwd(), "crypto_output"))

if st.button("Иштетүү", type="primary"):
    if not message.strip():
        st.warning("Сураныч, текст киргизиңиз.")
    else:
        aes_result = run_aes_demo(work_dir=work_dir, original_message=message)
        rsa_result = run_rsa_demo(original_message=message)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("AES (Симметриялык)")
            st.code(aes_result["key"], language="text")
            st.write(f"**Аткарылуу убактысы:** {aes_result['duration']:.6f} секунд")
            st.write(f"**Шифрленген файл:** `{aes_result['file_path']}`")
            st.text_area("AES шифрленген текст (кыскартылган)", value=str(aes_result["cipher_text"][:120]), height=90)
            st.success(f"AES дешифрленген текст: {aes_result['decrypted_text']}")

        with col2:
            st.subheader("RSA (Асимметриялык)")
            st.write(f"**Шифрленген текст узундугу:** {rsa_result['cipher_length']} байт")
            st.write(f"**Аткарылуу убактысы:** {rsa_result['duration']:.6f} секунд")
            st.text_area("RSA шифрленген текст (кыскартылган)", value=str(rsa_result["cipher_text"][:120]), height=90)
            st.success(f"RSA дешифрленген текст: {rsa_result['decrypted_text']}")

        st.subheader("Салыштыруу")
        faster = "AES" if aes_result["duration"] < rsa_result["duration"] else "RSA"
        st.info(f"Бул иштетүүдө ылдамыраак алгоритм: **{faster}**")
