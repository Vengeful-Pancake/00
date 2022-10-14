import random
import os
import speech_recognition as sr
import pyttsx3
import webbrowser


def ear():
    r = sr.Recognizer()
    print("speak ")
    try:
        # use the microphone as source for input.
        with sr.Microphone() as source2:
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)
            print("now")
             
            #listens for the user's input
            audio2 = r.listen(source2)
             
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
 
            print("\nDid you say "+MyText)
            return MyText
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occured")


def mouth(input):
    print("Answer: ")
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(input)
    engine.runAndWait()
    return 0

def mind(input):
    if "hello" in input:
        return "Hello administrator, what can I do for you today?",1
    if "shutdown" in input:
        RunAsAdmin('bat/shutdown.bat','arg1','arg2')
        return "the computer will be shutdown in an hour. Thank you for using me today, administrator.",0
    if "random" in input:
        sr = random.randint(1,100)
        return str(sr),1
    if "search"in input:
        url = 'https://codefather.tech/blog/'
        webbrowser.open(url)

def RunAsAdmin(path,*args):
	os.system(r'Powershell -Command "Start-Process "'+path+'"'+ # CMD running Powershell
				' -ArgumentList @('+str(args)[1:-1]+')'+ # Arguments. [1:-1] to remove brackets
				' -Verb RunAs"' # Run file as administrator
    )

