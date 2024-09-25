import streamlit as st
import google.generativeai as genai
from random import randint

genai.configure(api_key="AIzaSyBgsUCq61-50kMRGCFL3JorK1vYUzTPQfs")
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_response(s):
    print("User:",s)
    response = model.generate_content(s)
    text = str(response.text).replace("```","```\n").replace('* **', '- **')

    if hasattr(response, 'candidates') and response.candidates:
        finish_reason = response.candidates[0].finish_reason
        print(f"Finish reason: {finish_reason}")

    return add_Yergali(text)

def add_Yergali(response_text):
    smiles = ['😏','😎','🤖','🦾','🏋️','🥇']
    rr = randint(0,len(smiles)-1)
    smile = smiles[rr]
    if "I am a large language model" in response_text:
        response_text += " But, @Yergalife helped me. "+smile
    elif "үлкен тіл моделімін." in response_text:
        response_text += " Бірақ, Ерғали ағай мені жасақтап шығарды. "+smile
    elif "үлкен тілдік моделімін." in response_text:
        response_text += " Бірақ, Ерғали ағай мені жасақтап шығарды. "+smile
    elif "үлкен тіл модельмін." in response_text:
        response_text += " Бірақ, Ерғали ағай маған шыңдалуыма көмектесті. "+smile
    elif "үлкен тілдік модельмін." in response_text:
        response_text += " Бірақ, Ерғали ағай маған шыңдалуыма көмектесті. "+smile
    elif "Я большая языковая модель" in response_text:
        response_text += " Но, Ергали агай основал меня. "+smile
    elif "Я — большая языковая модель" in response_text:
        response_text += " Но, Ергали агай помог мне реализоваться. "+smile 
    return response_text

# Set the page to wide mode
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
    st.header("Біздің жауапты қабыл алыңыз:")
    st.write(response_text)
