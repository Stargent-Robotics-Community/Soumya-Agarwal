import random
import pyttsx3
import speech_recognition as sr

a = pyttsx3.init()
a.say("Hello, I am a basic bot! How can I help you?")
a.runAndWait()
a.stop()

a.setProperty('rate', 150)

r = sr.Recognizer()

wish = ['hey there', 'hello', 'hi', 'hey!', 'hey']
question1 = ['how are you']
question2 = ['who made you', 'who created you']
answer2 = ['I was created by Soumya Agarwal for practice']
question3 = ['who are you', 'what is you name']
question4 = ['you are very useful']
answer4 = ['your welcome', 'glad to help you']
exit = ['exit', 'close', 'goodbye', 'shutdown']

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    r.pause_threshold = 1
    print("Speak now")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio)
    print(text)
    a.say(text)
    a.runAndWait()
except:
    print("Sorry I can't understand please try again")

if text in wish:
    random_wish = random.choice(wish)
    print(random_wish)
    a.say(random_wish)
    a.runAndWait()

elif text in question1:
    a.say('I am fine')
    a.runAndWait()
    print('I am fine')

elif text in question2:
    a.say(answer2)
    a.runAndWait()
    print(answer2)

elif text in question4:
    random_answer4 = random.choice(answer4)
    print(random_answer4)
    a.say(random_answer4)
    a.runAndWait()

elif text in question3:
    a.say('I am bot, obviously')
    a.runAndWait()
    print('I am a bot, obviously')

elif text in exit:
    print('see you later')
    a.say('see you later')
    a.runAndWait()
    exit()

else:
    a.say("I don't know the answer to your question may be updated version may help you stay in contact")
    a.runAndWait()
    print('I do not know the answer to your question may be updated version may help you!! , stay in contact')