import speech_recognition as sr
import pyautogui

r=sr.Recognizer()
with sr.Microphone() as source:
    while True:
        print("Listening")
        audio=r.listen(source)
        print("Recognising")
        try:
            text=r.recognize_google(audio)
            pyautogui.typewrite(text)
        except:
            pass


