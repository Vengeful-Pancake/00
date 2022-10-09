import random
import os
import speech_recognition
import pyttsx3

def mouth():
    print("Answer: ")
    return 0

def ear():
    print("I am listening")

    return 0

def mind(input):
    if "hello" in input:
        return "Hello administrator, what can I do for you today?",1
    if "shutdown" in input:
        RunAsAdmin('bat/shutdown.bat','arg1','arg2')
        return "the computer will be shutdown in an hour. Thank you for using me today, administrator.",0
    if "random" in input:
        str = random.randint(1,100)
        return str(str),1

def RunAsAdmin(path,*args):
	os.system(r'Powershell -Command "Start-Process "'+path+'"'+ # CMD running Powershell
				' -ArgumentList @('+str(args)[1:-1]+')'+ # Arguments. [1:-1] to remove brackets
				' -Verb RunAs"' # Run file as administrator
    )

