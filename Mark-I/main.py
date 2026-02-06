from ears import listen
from intent import handle_input
from intent import wish_me
from hotword import listen_for_hotword
from mouth import speak
import hotword

while True:
    while not hotword.is_awake:
        if listen_for_hotword():
            hotword.is_awake=True
            print("Awake.")
            wish_me()
        continue


    speak("Listening...")
    command=listen()
    print("You: ",command)

    if "sleep" in command:
        hotword.is_awake=False
        speak("Going to sleep.")
        continue

    handle_input(command)