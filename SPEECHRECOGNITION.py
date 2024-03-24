import speech_recognition as sr
import webbrowser as w
r=sr.Recognizer()
with sr.Microphone() as source:
    print("speak now...")
    audio=r.listen(source)

try:
    text=r.recognize_google(audio)
    print("Tell something:"+text)
    w.open("https://www.google.com/search?q=" + text)
except sr.UnknownValueError:
    print("could not understand the audio")
except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


