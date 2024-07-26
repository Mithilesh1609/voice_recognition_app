## initialize the requirements...
import speech_recognition as speech_rec
import pyttsx3
import os

from error_codes import audioNotFoundError

# Initialize the voice recognizer
recognizer = speech_rec.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties for the voice (male voice)
voices = engine.getProperty('voices')
for voice in voices:
    try:
        if 'male' in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    except Exception as e:
        raise audioNotFoundError

# Simple rule-based responses
def get_response(query):

    ## converting the query string into lowercase
    query = query.lower()
    
    ## checking for different key phrases and assigning them responses accordingly...
    if "hello" in query:
        return "Hello! How can I help you today?"
    elif "what do you do" in query:
        return "I'm an AI assistant, so I'm here to help you!"
    elif "what is your name" in query:
        return "I am your AI assistant."
    elif ("close" in query or "end" in query or "stop" in query):
        return "Goodbye!"
    else:
        return "I'm sorry, I don't understand that."

def listen():
    with speech_rec.Microphone() as source:
        print("Listening...")

        ## trying to adjust for the ambient noise for clear voice by removing unwanted noice.
        recognizer.adjust_for_ambient_noise(source)

        ## strating listing with recognizers
        audio = recognizer.listen(source)
        
        try:
            print("Recognizing...")

            ## getting processed by google web speech locally... 
            query = recognizer.recognize_google(audio)
            print(f"User said: {query}")
            return query
        except speech_rec.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except speech_rec.RequestError:
            print("Sorry, my speech service is down.")
            return None

def respond(text):
    engine.say(text)
    engine.runAndWait()

def main():
    print("AI Voice Assistant is running...")
    while True:
        query = listen()
        if query:
            response_text = get_response(query)
            print(f"AI: {response_text}")
            respond(response_text)
            if ("close" in query.lower() or "stop" in query.lower() or "end" in query.lower()):
                print("Closing the application...")
                break

if __name__ == "__main__":
    main()