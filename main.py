import speech_recognition as sr  # type: ignore
import webbrowser
import pyttsx3                   # type: ignore  --> it is used to speak out text
import musiclib
import requests                  # type: ignore
from openai import OpenAI        # type: ignore    

recognizer = sr.Recognizer()     #initializing recognizer
engine = pyttsx3.init()          #initializing pyttsx .init
newsapi = "983fa42b98554ef0af68824ed7b2948c"

def speak(text):
    engine.say(text)
    engine.runAndWait()          #wihtout this funtion it won't hold the text speaking
r = sr.Recognizer()
 
def Aiprocessgpt(command):
    client = OpenAI( api_key = "")
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        massage =[
            {"role":"system","content":"you are virtual assistent"},
            {"role":"view","content": command}
    ]
    )
    return completion.choices[0].message.content  
 
 
 
 
 
def processcommand(c):
    print(c)    
    if "open google" in c.lower():
       webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
       webbrowser.open("https://youtube.com")
       
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclib.music[song]
        webbrowser.open(link)
        
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        data = r.json()
        articles = data.get("articles",[]) 
        for article in articles[:3]:
         speak(article['title'])
  
    else:
        #let chatgpt handle the request
        output = Aiprocessgpt(c)
        speak(output)
  
    


if __name__ == "__main__":
    print("Initializing jaarvvis....")
    speak("Initializing jaarvvis....") 

    while(True):
       
        try:
            # Use the microphone as source for input
            with sr.Microphone() as source:
             r.adjust_for_ambient_noise(source, duration=0.5) 
             print("Listening...")
             # Inside this upper block, the microphone is active and capturing audio
        
             # Capture the audio from the microphone
             audio = r.listen(source , timeout=3,phrase_time_limit=3)
    
            # Recognize the speech using Google Web Speech API
             text = r.recognize_google(audio)
             print(f"You said: {text}")
        
             #trigger to activate
             if(text.lower() == "jarvis"):
                 speak("Hello sir")
                 
                 #listen for command   
                 with sr.Microphone() as source:
                     print("Jarvis Actived")
                     audio = r.listen(source, phrase_time_limit=4)
                     command = r.recognize_google(audio)
                   
                     processcommand(command) 
                     
        except Exception as e:
            print("Error;{0}".format(e))
        except sr.RequestError:
                print("Sorry, the service is unavailable or there's an issue with the API.")
                
                
              