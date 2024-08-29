import speech_recognition as sr 
recognizer = sr.Recognizer()
def mic1():
	with sr.Microphone(device_index=0) as source :
		print ("Say something: ")
		recognizer.adjust_for_ambient_noise(source)

		audio = recognizer.listen(source)
		print ("Recognizing....")
		text = recognizer.recognize_google(audio)
		print ("You said: ",text)
		return text
if __name__ == "__main__":
	mic1()
"""import speech_recognition as sr
index = 0
for name in sr.Microphone.list_microphone_names():
	print(index,":",name)
	index = index + 1"""
