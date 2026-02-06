import pyttsx3

engine=pyttsx3.init()

def speak(text):
    print("Mark I: ",text)
    engine.setProperty('rate', 200)
    engine.say(text)
    engine.runAndWait()