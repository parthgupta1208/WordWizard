import speech_recognition as sr
import pyautogui
import threading

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
    pyautogui.typewrite(text,0.1)

t1 = threading.Thread(target=listen)
t1.start()
