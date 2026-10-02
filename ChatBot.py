#pip install streamlit openai
#streamlit run ChatBot.py

import streamlit as st

st.write("## ChatBot de IA")

mensagem_usuario = st.chatbot_input = st.text_input("Escreva sua mensagem aqui...")
print(mensagem_usuario)