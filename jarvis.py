import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)


if __name__ == "__main__":
    speak("initializing jarvis")


while True:
    recog = sr.Recognizer()

    print("recognizing")
    try:
        with sr.Microphone() as source:
            recog.adjust_for_ambient_noise(source)
            audio = recog.listen(source, timeout=1.8, phrase_time_limit=1.2)
            print("Lestening...")
        word = recog.recognize_google(audio)

        if(word.lower() == "jarvis"):
            speak("yes sir")

            with sr.Microphone() as source:
                recog.adjust_for_ambient_noise(source)
                audio = recog.listen(source)
                recog.pause_threshold=1
                print("Jarvis Active...listenning for command")
                
                
            command = recog.recognize_google(audio)
            processcommand(command)


    except Exception as e:
        print("Error; {0}".format(e))