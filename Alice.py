#This is a basic code of AI


import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
# import smtplib

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
#----------------------use for Male voice-------------------
# print(voices[0].id)
engine.setProperty('voice', voice[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Alice, Ayush sir, Please tell me how may I help you")
def takeCommand():
    #it takes microphone input from the user and returns string output


    ear = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        ear.pause_threshold = 1
        audio = ear.listen(source)

    try:
        print("Recognizing...")
        query = ear.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
    # Logic for executing takes based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
    #give your command and then say 'according to wikipedia'
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google chrome browser' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        

        # elif 'play music' in query:
        #     music_dir = 'D\\Non Critical\\songs\\Favorite Songs2'
        #     songs = os.listdir(music_dir)
        #     os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Ayush, Sir, the time is {strTime}")

        # elif 'open code' in query:
        #     codePath = 'Put your vscode path'
        #     os.startfile(codePath)

       