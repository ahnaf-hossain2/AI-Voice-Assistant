import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def talk(words):
    engine.say(words) # Queue a command to speak an utterance
    engine.runAndWait() # Blocks while processing all the currently queued commands
def processCommand(c):
    if "Open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "Open YouTube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "Open Facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "Open Instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
    elif "Open Twitter" in c.lower():
        webbrowser.open("https://www.twitter.com")
    elif "Open LinkedIn" in c.lower():
        webbrowser.open("https://www.linkedin.com")

if __name__ == "__main__":
    talk("Hello!I'm Oval. How can I help you?")
    while True:
        # Listen to the wake word "Oval"
        # Obtain audio from the microphone
        r = sr.Recognizer()

        # Recognize speech using Google Speech Recognition
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Hearing...")
                audio = r.listen(source, timeout=3, phrase_time_limit=1)
            command = r.recognize_google(audio)
            if(command.lower() == "Oval"):
                talk("Yes")
                # Listen for command
                with sr.Microphone() as source:
                    print("Oval Running...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
