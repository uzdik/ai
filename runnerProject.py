import streamlit as st
import google.generativeai as genai
from random import randint

genai.configure(api_key="AIzaSyBgsUCq61-50kMRGCFL3JorK1vYUzTPQfs")
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_response(s):
    print(s)
    response = model.generate_content(s)
    text = str(response.text).replace("```","```\n").replace('* **', '- **').strip()
    return add_Yergali(text)

def add_Yergali(response_text):
    smiles = ['😏','😎','🤖','🦾','🏋️','🥇']
    rr = randint(0,len(smiles))
    smile = smiles[rr]
    if "I am a large language model" in response_text:
        response_text += " But, @Yergalife helped me. "+smile
    elif "үлкен тіл моделімін." in response_text:
        response_text += " Бірақ, Ерғали @Yergalife ағай мені жасақтап шығарды. "+smile
    elif "үлкен тілдік моделімін." in response_text:
        response_text += " Бірақ, Ерғали @Yergalife ағай мені жасақтап шығарды. "+smile
    elif "үлкен тіл модельмін." in response_text:
        response_text += " Бірақ, Ерғали @Yergalife ағай маған шыңдалуыма көмектесті. "+smile
    elif "үлкен тілдік модельмін." in response_text:
        response_text += " Бірақ, Ерғали @Yergalife ағай маған шыңдалуыма көмектесті. "+smile
    elif "Я большая языковая модель" in response_text:
        response_text += " Но, Ергали @Yergalife агай основал меня. "+smile
    elif "Я — большая языковая модель" in response_text:
        response_text += " Но, Ергали @Yergalife агай помог мне реализоваться. "+smile 
    return response_text

# Set the page to wide mode
st.set_page_config(layout="wide")

# Hide Streamlit's header and 'Manage App' button
hide_streamlit_style = """
    <style>
    /* Hide the hamburger menu */
    #MainMenu {visibility: hidden;}
    
    /* Hide the Streamlit header */
    header {visibility: hidden;}
    
    /* Hide the Streamlit footer */
    footer {visibility: hidden;}

    /* Hide specific app elements that might have changed */
    .css-1cm3hpy {visibility: hidden;}  /* Targets specific container for 'Manage App' */
    .css-18ni7ap {visibility: hidden;}  /* Another potential class for buttons */
    </style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)


st.title("Үздік Білім GenAI")
question  = st.text_input("Сұрағыңызды осында жазсаңыз:")

if question:
    response_text = generate_response(question)
    print(response_text)
    st.header("Біздің жауапты қабыл алыңыз:")
    st.write(response_text)
