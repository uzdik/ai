import streamlit as st
from helper import generate_response

st.set_page_config(layout="wide")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}  
footer {visibility: hidden;}   
header {visibility: hidden;}   
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("Үздік Білім GenAI")
question  = st.text_input("Сұрағыңызды осында жазсаңыз:")

if question:
    response_text = generate_response(question)
    print(f"GenAI: {response_text}\n{'*'*20}")
    st.write(response_text)

