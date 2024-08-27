import pyttsx3
import aitest
import speech_recognition as sr

#Initialize speech recognition
r = sr.Recognizer()

#Sets up text to speech
def speak(text):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)

    engine.say(text)
    engine.runAndWait()


#Main method
if __name__ == "__main__":
    #Loads context and prompts from prompt.txt
    context_file = "prompt.txt"
    context_messages = aitest.load_context_from_file(context_file)

    while True:
        try:


            with sr.Microphone() as source2:

                #Adjusts for ambient noise
                r.adjust_for_ambient_noise(source2, duration=0.1)
                print("Listening...")

                #Listens to the audio
                audio2 = r.listen(source2, timeout=3, phrase_time_limit = 5)

                #Converts audio to text
                user_input = r.recognize_google(audio2)
                user_input = user_input.lower()
                print ("User:", user_input)


            #user_input = input ("User: ")
            if user_input.lower in ["quit", "exit", "bye"]:
                False
            #Feeds user input into AI to get a response back in text to speech
            response = aitest.chat_with_gpt(user_input, context_messages)
            print("Response: ", response)
            speak(response)
        except sr.RequestError as e:
            print("Could not request results")
        except sr.UnknownValueError:
            print("Unknown error occured")