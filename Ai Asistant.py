#from tkinter.tix import InputOnly
#from unittest import result
import pyttsx3
import wikipedia

# let name of our assistance will be 'jarvis'

jarvis = pyttsx3.init()
voices = jarvis.getProperty('voices')
jarvis.setProperty('voice', voices[1].id)
jarvis.setProperty('rate', 175)     # for male voice

In = input("search Wikipedia/Google: ")
Input = input("In how many lines you want your result: ")
result = wikipedia.summary(In, sentences = Input)
jarvis.say("According to Wikipedia")
print(result)
jarvis.say(result)
jarvis.say("Thank you for using me! ")
jarvis.runAndWait()
