from programy.clients.embed.basic import EmbeddedBasicBot
from programy.clients.embed.basic import EmbeddedDataFileBot
import requests
import pyttsx3
import speech_recognition as sr
#Initialize the recognizer
set = False
r = sr.Recognizer()
import requests
import json

id = 1234567890
def SpeakText(command):
	#Initialize engine
	engine=pyttsx3.init()
	#Voice properties
	engine.setProperty("voice","german")
	#speech
	engine.say(command)
	engine.runAndWait()

while True:
	print("Input:")
	message = input()
	x = requests.get('http://0.0.0.0:8989/api/rest/v1.0/ask?question=' + message + '&userid=' + str(id))
	json_data = x.json()['response']
	question = json_data['question']
	answer = json_data['answer']
	print(answer)
	SpeakText(answer)
	

set = False
