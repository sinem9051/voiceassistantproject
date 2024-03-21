import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from my_voice_assistant_ui import Ui_MainWindow
import speech_recognition as sr
import pyttsx3
import webbrowser
from newsapi import NewsApiClient
import pyowm

class MyVoiceAssistant(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyVoiceAssistant, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('My Voice Assistant')

        self.r = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', 'english')
        self.newsapi = NewsApiClient(api_key='e25cebfc461c4375b64b2eeca1302b9f')
        self.owm = pyowm.OWM('5b7951aba339553b6b998a9034816a98')
        self.weather_manager = self.owm.weather_manager()

        self.pushButton.clicked.connect(self.handle_command)
        self.microphoneButton.clicked.connect(self.start_listening)

    def start_listening(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.r.listen(source)
        try:
            text = self.r.recognize_google(audio, language="en-US")
            self.lineEdit.setText(text.lower())
            self.handle_command()  # Otomatik olarak komutu işle
        except sr.UnknownValueError:
            self.lineEdit.setText("")
            print("Could not understand audio")
        except sr.RequestError as e:
            self.lineEdit.setText("")
            print("Error: {0}".format(e))

    def say(self, text):
            self.engine.say(text)
            self.engine.runAndWait()
    
    def handle_command(self):
        command = self.lineEdit.text().lower()
        if command:
            if command == "stop":
                self.say("Stopping the assistant. Goodbye!")
                sys.exit()

            commands = {
                "hello": self.say_hello,
                "how are you": self.say_how_are_you,
                "i am fine": self.say_good,
                "thank you": self.say_youre_welcome,
                "goodbye": self.say_goodbye,
                "google": self.open_google,
                "youtube": self.open_youtube,
                "news": self.get_news,
                "weather": self.get_weather
            }
            if command in commands:
                commands[command]()
            else:
                self.say("Sorry, I didn't understand the command.")


    def say_hello(self):
        self.say("Hello!")

    def say_how_are_you(self):
        self.say("I'm fine, thank you. How are you?")

    def say_good(self):
        self.say("That's great! How can I help you?")

    def say_youre_welcome(self):
        self.say("You're welcome!")

    def say_goodbye(self):
        self.say("Goodbye! Have a nice day.")

    def open_google(self):
        webbrowser.open("https://www.google.com/")

    def open_youtube(self):
        webbrowser.open("https://www.youtube.com/")

    def get_news(self):
        top_headlines = self.newsapi.get_top_headlines(language='en', country='us')
        self.say("Here are the latest news from the United States:")
        for article in top_headlines['articles'][:5]:
            self.say(article['title'])

    def get_weather(self):
        observation = self.weather_manager.weather_at_place("Ankara,Turkey")
        weather = observation.weather
        temperature = weather.temperature('celsius')['temp']
        status = weather.status
        self.say("In Ankara, the weather is currently " + status + " with a temperature of " + str(temperature) + " degrees Celsius.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MyVoiceAssistant()
    mainWindow.show()
    sys.exit(app.exec_())
