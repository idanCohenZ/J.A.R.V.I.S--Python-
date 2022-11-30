import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes



# A note for the devs out there :
# You have to install in your environment the three imports above
# plus the pyaudio which is not available for python 3.6 and above
# to save yourself time- download python 3.6 exactly, know the root, add that version as interpreter
# and only then start installing the packages. (there is a way to install it on newer versions but believe
# me - save yourself the headaches)

engine = pyttsx3.init()
listener = sr.Recognizer()


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
            command = command.lower()

            if 'Alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command_text = take_command()
    print(command_text)
    if 'play' in command_text:
        song = command_text.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command_text:
        # Using the datetime object and applying a method to turn it to string
        # There is %H:M and I means the duel meaning, the P means am/pm
        time = datetime.datetime.now().strftime('%I:%M:%P')
        talk("the current time is: " + time)
    elif 'what the heck is' in command_text:
        search_item = command_text.replace('what the heck is', '')
        info = wikipedia.summary(search_item, 1)
        print(info)
        talk(info)
    elif 'are you single' in command_text:
        talk('Sorry, I am in a relationship with wifi')
    elif 'joke' in command_text:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'goodbye' in command_text:
        talk('goodbye')
    else:
        talk('Sorry, could you please repeat your wish?')


# In case you want to make her keep listening:
while True:
    run_alexa()
# run_alexa()
