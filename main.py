import speech_recognition as sr
import pyautogui
import threading
# from transformers import pipeline
from deepmultilingualpunctuation import PunctuationModel

# punctuator = pipeline("text-classification", model="textattack/bert-base-uncased-SST-2", tokenizer="bert-base-uncased")
model = PunctuationModel()


r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        while True:
            print("Listening...")
            audio = r.listen(source)
            print("Recognizing...")
            try:
                text = r.recognize_google(audio)
                print(f"You said: {text}")
                t2 = threading.Thread(target=type_text, args=(text,))
                t2.start()
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")

def type_text(text):
    # punctuated_text = punctuator(text)
    punctuated_text = model.restore_punctuation(text)
    pyautogui.typewrite(punctuated_text,0.1)

t1 = threading.Thread(target=listen)
t1.start()
