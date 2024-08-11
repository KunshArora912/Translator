import pyttsx3
import speech_recognition as sr
from googletrans import Translator

engine = pyttsx3.init('sapi5')

def getvoices(voice):
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 150)
    if 0 < voice <= len(voices):
        engine.setProperty('voice', voices[voice - 1].id)

def Speak(audio):
    print("  ")
    engine.say(audio)
    print(f": {audio}")
    print("  ")
    engine.runAndWait()

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-IN")
        print(query)
    except sr.UnknownValueError:
        print("I did not understand, can you please repeat that")
        return "None"
    return query.lower()

def TakeHindi():
    line = takeCommandMic()
    return line

def Tran():
    Speak("What would you like to translate?")
    line = TakeHindi()
    if line != "None":
        translate = Translator()
        result = translate.translate(line)
        Text = result.text
        Speak(Text)
    else:
        Speak("I didn't catch that. Please try again.")

def main():
    Tran()

if __name__ == "__main__":
    main()
