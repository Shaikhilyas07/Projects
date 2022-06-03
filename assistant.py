from datetime import datetime
import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import smtplib

# from voice.jarvis import sendEmail
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak('Good evening')
    speak('I am jarvis sir. Please tell me how may i help you')


def takeCommand():
    '''it takes microphone input from the user'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            print('Say that again...')
            return 'none'

        return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ilyasshaikh987654@gmail.com', 'password here')
    server.sendmail('ilyasshaikh987654@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishMe()
    # takeCommand()
    if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir = 'F:\\family\\Areeba Anam\\Songs'
            Songs = os.listdir(music_dir)
            print(Songs)
            os.startfile(os.path.join(music_dir, Songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, The time is  {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\dell\\.vscode\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'send emai to' in query:
            try:
                speak('What should i say?')
                content = takeCommand()
                to = "ilyasshaikh987654@gamil.com"
                sendEmail(to, content)
                speak('Email has been sent!')

            except Exception as e:
                print(e)
                speak(
                    'Sorry my friend ilyas bhai. I am not able to send this email'
                )


    #logic for executing task based on querry
