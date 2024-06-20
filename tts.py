#pip install pyttsx3
import pyttsx3
text_speech =pyttsx3.init()
answer =input("What the text you want to convert")
text_speech.say(answer)
text_speech.runAndWait()