import webbrowser
import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import os
import smtplib

'''Iron man jarvis program'''

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    # speak("I am jarvis sir how may i help you")
    speak("me jarivs huun sir  me aapki madad kasay karu")

def takeCommand():
    #it take microphone input from the user and return a string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User Said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com,',587)
    server.ehlo()
    server.starttls()
    server.login('snehsingh2020@gmail.com','google3546')
    server.sendmail('snehsingh2020@mgail.com',to,content)
    server.close()
if __name__ == '__main__':
    wishMe()
    while True:
        query= takeCommand().lower()
        #logic for executing task based on
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'google khol' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir ='C:\\Users\\Aryan\\Music\\The Fast & Furious Soundtrack Collection - Vol.6 The Fast and the Furious Tokyo Drift (Original Motion Picture Soundtrack) (Expanded Version) (2 Cds) (Various Artist)'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        elif 'open code' in query:
            codePath="C:\\Users\\Aryan\\AppData\\Local\\Programs\\Python\\Python36\\pythonw.exe"
            os.startfile(codePath)
        elif 'email to sneh' in query:
            try:
                speak("what should i say?")
                content=takeCommand()
                to="snehsingh2020@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry my friend sneh bhai. i am not able to send this email")