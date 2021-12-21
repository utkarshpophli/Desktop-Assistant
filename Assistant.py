import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os 
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greeting():
    hour = int(datetime.datetime.now().hour)
    if hour >= 6 and hour <=12:
        speak("Good morning, Sir")

    elif hour >= 12 and hour <=18:
        speak("Good afternoon, Sir")
        
    else:
        speak("Good evening, Sir")

    speak("Hello, I am your assistant. How can i help you!!")

def inCommand():

    r =sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print(" ")
        query = r.recognize_google(audio, language='en-in')
        print(f"{query}\n")

    except Exception as e:
        print("Unable to understand, do try again")
        return 'None'
    return query

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 578)
    server.ehlo()
    server.starttls()
    server.login("email__@gmail.com", "Password")
    server.sendmail("email__@gmail.com", to,content)
    server.close()

if __name__ == "__main__":
    greeting()
    while True:
        query = inCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia ")
            print(results)
            speak(results) 
        
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
        elif 'open Google' in query:
            webbrowser.open("https://www.google.com/")
        elif 'open Gmail' in query:
            webbrowser.open("https://www.gmail.com/")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")
            print(speak)
        elif 'open vs code' in query:
            codePath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open zoom' in query:
            codePath = "C:\\Users\\Dell\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(codePath)
        elif 'open Github' in query:
            codePath = "C:\\Users\\Dell\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe"
            os.startfile(codePath)

        elif "send a mail" in query:
            try:
                speak("context for mail?")
                content = inCommand()
                to = "sendersmail@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                speak("Unable to send email")
                print("Unable to send email")