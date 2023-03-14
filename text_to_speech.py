import pyttsx3
engine = pyttsx3.init()
usertext = input("Input Text: ")
engine.say(usertext)
engine.runAndWait()