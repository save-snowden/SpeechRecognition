from gtts import gTTS
import os
import time
import playsound
import speech_recognition as sr
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

def speak1(text):
    tts = gTTS(text=text)
    filename = "voice1.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def speak2(text):
    tts = gTTS(text=text)
    filename = "voice2.mp3"
    tts.save(filename)
    playsound.playsound(filename)


with sr.Microphone() as source:
    print('[Search Youtube content creators: search Youtube]')
    speak1("talk to me now, what do you need to find?")
    print('Speak Now')
    audio = r3.listen(source)

    if 'creator' in r2.recognize_google(audio):
        speak2("PewDiePie isn't it?")
        r2 = sr.Recognizer()
        url = 'https://www.youtube.com/results?search_query='

        with sr.Microphone() as source:
            print('Piewds, Isnt It?')
            audio = r2.listen(source)

            try:
                get = r2.recognize_google(audio)
                print(get)
                wb.get().open_new(url+get)
            except sr.UnknownVaueError:
                print('error')
            except sr.RequestError as e:
                print('Failed'.format(e))
