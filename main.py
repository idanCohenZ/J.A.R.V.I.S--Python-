from datetime import datetime
import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyfirmata
from pymata4 import pymata4
import time
from time import sleep
from pyfirmata import SERVO

board = pymata4.Pymata4() # connect an arduino and find port
echoPin = 11
triggerPin = 12
engine = pyttsx3.init()
listener = sr.Recognizer()

# servo simple code
# port = ''
# servo_pin = 7
# board.digital[servo_pin].mode = SERVO
#
#
# def rotateServo(pin, angle):
#     board.digital[servo_pin].write(angle)
#     sleep(0.015)
#
#
# for i in range(0, 180):
#     rotateServo(servo_pin, i)
#     # in case you want it to return to normal position
# for i in range(180, 1, -1):
#     rotateServo(servo_pin, i)

#
# internet version that looks good - weather temperature:
# from pyfirmata import ArduinoMega
# from pyfirmata.util import Iterator
# import time
#
# board = ArduinoMega('/dev/ttyUSB0') # connect to arduino usb port
#
# iterator = Iterator(board) # start reading analog input
# iterator.start()
#
# pinTemp = board.get_pin('a:0:i') # set valid in analog pin
#
# while True:
#     voltage = pinTemp.read() # read voltage input
#     if voltage is not None: # first read after startup is somtimes None
#         temp = 5.0*100*voltage # convert voltage to temperature
#         print "{0} Celsius".format(temp)
#         time.sleep(1) # 1 second waiting
# ###



# engine.say("Good morning sir.")
# engine.runAndWait()


# In case you want a female voice
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if 'Alexa' in command:
                command = command.lower()
                command = command.replace('alexa', '')
            print(command)

    except:
        pass
    return command


# internet version that looks good - distance with ultra - sonic:
def check_distance():
    board.set_pin_mode_sonar(triggerPin, echoPin, the_callback)
    print("entered check distance")
    while True:
        try:
            time.sleep(1)
            board.sonar_read(triggerPin)
        except Exception:
            print("error")


def the_callback(data):
    print("Distance ", data[2])








def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    if 'distance' in command:
        check_distance()


run_alexa()





# Py + Arduino trial
# my try at translating
# trigPin = 8
# echoPin = 9
# #defining variables
# near=6; # red -as in proximity alert
# far=7;  # green- as in all good
# board.digital[echoPin].mode = pyfirmata.INPUT
#
# duration = pulseIn(echoPin, HIGH);
