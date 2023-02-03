import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[10].id)

# convert my voice to virtual voice
def talk(text):
    engine.say(text)
    engine.runAndWait()

#voice command here (speak)
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)  #listener listen the user-voice by source
            user_command = listener.recognize_google(voice)  #by google-api, listener send audio & google back it like text
            print('user_command: ',user_command)
            # command = command.lower()
            # if 'alexa' in command:
            #     command = command.replace('alexa', '')
            #     # print(command)
            #     print('user_command', command)
    except:
        pass
    return user_command

def run_assistant():
    command = take_command()
    print('get_user_command: ',command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing'+ song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is :' + time)
        print(time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 3) # 3 = take 3 lines of data from wikipedia
        print(info)
        talk(info)

    elif 'what is' in command:
        search = command.replace('what is', '')
        talk('search' + search)
        pywhatkit.search(search)

    if 'hello' in command:
        talk('Hi there')
        print('Hi there')

    else:
        talk('Please say the command again')

while True:
    run_assistant()

