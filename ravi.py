import pyttsx3
from pyttsx3 import engine
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes
listner = sr.Recognizer()
engine = pyttsx3.init()
def talk(x):
  engine.say(x)
  engine.runAndWait()
talk('hi, i,am, ravi . what is your name')
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening..")
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command= command.lower()
            print(command)
            if "ravi" in command:
              command =command.replace('ravi','') 
               
    except:
        pass
    return command
def run_ravi():
  command=take_command()
  if 'hi i am' in command:
      command=command.replace('hi i am','') 
      talk("how are you doing"+command)
  elif 'fine you' in command:
    talk("yeah,i,am,also fine")
    talk("what can i do for you ")  
  elif 'time' in command:
      time = datetime.datetime.now().strftime('%I:%M %p')
      talk(time)
  elif 'date' in command:
      time = datetime.today()
  elif 'say about' in command:
        person = command.replace('say about','')
        info = wikipedia.summary(person,3)
        talk(info)
  elif 'tell me the joke' in command:
      talk(pyjokes.get_jokes())
  elif 'play' in command:
      command=command.replace('play','')
      command=command.replace('song','')
      talk("playing "+command)
      pywhatkit.playonyt(command)
  else:
     talk("command is not found try again")
while (True):
  run_ravi()