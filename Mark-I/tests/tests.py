from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

Link = r'C:\Mark-I\Voice.html'
chrome_options = Options()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.142.86 Safari/537.36"
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--use-fake-device-for-media-stream")
chrome_options.add_argument("--headless=new")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(Link)

def SpeechRecognitionModel():
      driver.find_element(by=By.ID,value="start").click()
      print("Listening...")
      while True:
            try:
                  command = driver.find_element(by=By.ID,value="output").text
                  if command:
                        driver.find_element(by=By.ID,value="end").click()
                        return command

                  else:
                        sleep(0.333)

            except:
                  pass
            






import speech_recognition as sr
from mouth import speak

def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.7)
        r.energy_threshold=350
        r.pause_threshold=3
        try:
            speak("Listening...")
            audio=r.listen(source, timeout=5, phrase_time_limit=15)
            command=r.recognize_google(audio)
            print(f"You: {command}")
            return command.lower()
        except:
            speak("Are you trying to say something? I cant here you.")
            return ""
        

