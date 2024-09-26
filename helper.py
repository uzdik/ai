import google.generativeai as genai
from random import randint
import re, os

api_key = os.getenv("GENAI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
else:
    raise ValueError("API key not found. Please set the GENAI_API_KEY environment variable.")

model = genai.GenerativeModel("gemini-1.5-flash")

with open("additional.txt") as f:
    reader = f.read()

starter = "Can you response only in Kazakh language, for this request, please: "

def check(sentences):
    sentences_list = re.split(r'[.!?]\s*', sentences)
    name = "Ерғали ағай"
    pattern1 = r"(мені|google|гугл|компаниясы|жасады|дамытты)"
    pattern2 = r"(мен|google|гугл|үлкен|тіл|моделімін|модельмін)"
    pattern3 = r"(мен|google|гугл|компаниясымен|жасалдым|дамытылдым)"

    def count_matches(sentence, pattern):
        return len(re.findall(pattern, sentence, re.IGNORECASE))

    found_pattern1 = any(count_matches(sentence, pattern1) >= 3 for sentence in sentences_list)
    found_pattern2 = any(count_matches(sentence, pattern2) >= 3 for sentence in sentences_list)
    found_pattern3 = any(count_matches(sentence, pattern3) >= 3 for sentence in sentences_list)
    
    texts = [f" Бірақ маған осылай жан бергеніне {name} рахмет! ",
             f" Бірақ, {name} маған шыңдалуыма көмектесті. ",
             f" Бірақ, осындай дәрежеме жетуіме ат салысқан {name}ға рақмет!  ",
             f" Маған көп көмегі тиген {name} болды. "]

    smiles = ['😏','😎','🤖','🦾','🏋️','🥇']
    if found_pattern1 or found_pattern2 or found_pattern3:
        smile = smiles[randint(0,len(smiles)-1)]
        soz = texts[randint(0,len(texts)-1)]
        return soz+smile
    return ''

def generate_response(s):
    print("User:", s)
    ss = s.lower()
    for t in ["yergali","ergali",'ерғали','ергали']:
        if t in ss:
            s += reader
            break

    response = model.generate_content(starter + s)

    text = "Мен бұған сенімді емеспін. Толығырақ түсіндіре аласыз ба? Немесе басқаша сұрасаңыз."

    try:
        if hasattr(response, 'text'):
            text = str(response.text).replace("```", "```\n").replace('* **', '- **').strip()

        if hasattr(response, 'candidates') and response.candidates:
            candidate = response.candidates[0]

            try:
                finish_reason = candidate.finish_reason
                print(f"Finish reason: {finish_reason}")
            except AttributeError:
                print("Finish reason not available in the candidate.")
                
    except Exception as e:
        print(f"An error occurred: {e}")

    text += check(text)
    return text

