import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError:
            print("Sorry, I couldn't request results at the moment. Please try again later.")
            return ""

# Main function
def main():
    while True:
        command = listen()

        if "hello" in command:
            speak("Hello! How can I help you?")
        elif "bye" in command:
            speak("Goodbye!")
            break
        elif "open google" in command:
            speak("Opening Google...")
            import webbrowser
            webbrowser.open("https://www.google.com/")
        elif "jay shree ram" in command:
            speak("jay shree ram")
        elif "how are you" in command:
            speak("Hey I am Jaimin Sir's Personal Assistant, How can i help you?")
        elif "who are you" in command:
            speak("I am Personal Assistant, created by Jaimin Rathod Sir")
        elif "where are you from" in command:
            speak("I am  from your computer, stupid guys")
        elif "open youtube" in command:
            speak("Opening YouTube...")
            import webbrowser
            webbrowser.open("https://www.youtube.com/")
        else:
            speak("I am really sorry, Please say again.")

if __name__ == "__main__":
    main()
