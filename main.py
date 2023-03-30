# Importing Modules
import speech_recognition as sr
import pyautogui
import threading
## from transformers import pipeline
from deepmultilingualpunctuation import PunctuationModel

# Initializing the Punctuator Engine
## punctuator = pipeline("text-classification", model="textattack/bert-base-uncased-SST-2", tokenizer="bert-base-uncased")
model = PunctuationModel()

# Setup Speech Listener
r = sr.Recognizer()

# Function for Continual Listening
def listen():
    with sr.Microphone() as source:
        while True:
            print("Listening...")
            audio = r.listen(source)
            print("Recognizing...")
            try:
                # Recognise using google engine
                text = r.recognize_google(audio)
                print(f"You said: {text}")
                # Starting Punctuate & Type
                t2 = threading.Thread(target=type_text, args=(text,))
                t2.start()
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                pass

# Function for Punctuating & Typing the Text
def type_text(text):
    # punctuated_text = punctuator(text)
    punctuated_text = model.restore_punctuation(text)
    pyautogui.typewrite(punctuated_text,0.1)

# Starting the Listener Thread
t1 = threading.Thread(target=listen)
t1.start()
