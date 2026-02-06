import os
from mouth import speak
from brain import ask_ai, classify_intent
import datetime
import random

apps = {
    "chrome": "start chrome",
    "notepad": "start notepad",
    "calculator": "start calc",
    "spotify": "start spotify",
    "youtube": "start https://www.youtube.com/",
    "instagram": "start https://www.instagram.com",
}
wishes = [
    "online and ready sir.",
    "welcome back sir.",
    "at your service sir."
]

def wish_me():
    speak(random.choice(wishes))

def handle_input(command):
    intent = classify_intent(command)

    print(f"[INTENT]: {intent}")

    if intent == "command":
        return run_command(command)

    else:
        response = ask_ai(command)
        speak(response)

def run_command(command):

    if "open" in command or "launch" in command or "start" in command:
        found=False

        for app in apps:
            if app in command:
                speak("Opening")
                os.system(apps[app])
                found=True
                break

        if not found:
            print("I can't open that yet.")

    elif "time" in command:
        x=datetime.datetime.now()
        x=x.strftime("%I%M%p")
        speak(f"the time is {x}")

    elif "exit" in command:
        speak("Goodbye sir.")
        exit()

