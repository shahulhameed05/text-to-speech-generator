import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

while True:
    text = input("Enter your text (or type 'exit' to quit): ")
    if text.lower() == "exit":
        print("Exiting the program.")
        break
    speak(text)
