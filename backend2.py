
import os
import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import time
import requests
from bs4 import BeautifulSoup
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

emaildetailsDict = {
    "daksh": "s.daksh.rathi@fountainheadschools.org",
    "vedant": "s.vedant.dhameliya@fountainheadschools.org",
    "anant": "s.anant.jain@fountainheadschools.org",
    "dhaval sir": "s.dhaval.vagh@fountainheadschools.org",
    "shashank sir": "s.shashank.ray@fountainheadschools.org",
    "tejas sir": "s.tejas.gamit@fountainheadschools.org",
    "dhairya": "s.dhairya.garg@fountainheadschools.org",
    "ipshita": "s.ipsita.pansari@fountainheadschools.org",
    "mukund": "s.mukund.chandak@fountainheadschools.org",
    "pankaj": "pansaripankaj@gmail.com",
    "parents of jahhan": "p.jahhan.pansari@fountainheadschools.org",
    "self": "s.jahhan.pansari@fountainheadschools.org",
}

app_paths = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "spotify": r"C:\Users\Admin\AppData\Roaming\Spotify\Spotify.exe",
    "vscode": r"C:\Users\Admin\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "discord": r"C:\Users\Admin\AppData\Local\Discord\app-1.0.9150\Discord.exe",
    "file manager": r"C:\Windows\explorer.exe",
    "notepad": r"C:\Windows\notepad.exe",
    "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
    "excel": r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
    "powerpoint": r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE",
    "steam": r"C:\Program Files (x86)\Steam\steam.exe",
    "whatsapp": r"C:\Users\Admin\AppData\Local\WhatsApp\WhatsApp.exe",
    "blender": r"E:\Blender\blender-4.1....11-windows-x64\blender.exe"
}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand(timeout=5, phrase_time_limit=7):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙 Listening...")
        audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)

    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query.lower()
    except Exception:
        return "none"


def compose_mail():
    speak("Who would you like to send the mail to?")
    recipient_name = takeCommand()
    if recipient_name == "none":
        speak("Please try again.")
        return

    to = emaildetailsDict.get(recipient_name.lower())
    if not to:
        speak(f"I couldn’t find an email for {recipient_name}. Please say the email address.")
        to = takeCommand()

    speak("What is the subject of your email?")
    subject = takeCommand()
    if subject == "none":
        subject = ""

    speak("What do you want to say in the mail?")
    body = takeCommand()
    if body == "none":
        body = ""

    mail_url = (
        f"https://mail.google.com/mail/?view=cm&fs=1"
        f"&to={to}"
        f"&su={subject.replace(' ', '%20')}"
        f"&body={body.replace(' ', '%20')}"
    )

    speak(f"Opening Gmail to send your mail to {recipient_name}.")
    webbrowser.open(mail_url)

def open_first_result(query):
    print(f"Searching for '{query}'...")
    url = "https://duckduckgo.com/html/"
    params = {"q": query}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    response = requests.get(url, params=params, headers=headers)
    if response.status_code != 200:
        print("Error fetching results.")
        return

    # Parse results manually
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.select('.result__a')

    if not results:
        print("No results found.")
        return

    first_link = results[0]['href']
    print(f"Opening: {first_link}")
    webbrowser.open(first_link)


def open_application(query):

    from groq import Groq

    client = Groq(api_key="API_KEY_HERE")

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Only output the direct link of the website asked. No text, no extra words."},
            {"role": "user", "content": query}
        ],
        stream=True
    )

    for chunk in completion:
        if chunk.choices[0].delta.content:
            responseonquery = chunk.choices[0].delta.content, end=""
            print(responseonquery)
            webbrowser.open(responseonquery)




def executeCommand(query):
    if 'send a mail' in query:
        compose_mail()

    elif 'wikipedia' in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        try:
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        except Exception:
            speak("Sorry, I couldn't find any results.")

    elif 'open' in query or 'start' in query or 'launch' in query or 'play' in query:
        open_application(query)

    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")

    elif 'what is my name' in query:
        speak("Your name is Jahhan Pansari")

    else:
        speak("Sorry, I didn’t understand the command.")
        main_cycle()


def sleep_and_listen():
    speak("Going to sleep mode.")
    print("💤 Sleeping... Waiting for wake word 'assistant'...")
    while True:
        try:
            query = takeCommand(timeout=None, phrase_time_limit=4)
            if query == "assistant quit" or "bye assistant":
                quit
            if 'assistant' in query:
                speak("Yes, I’m here!")
                main_cycle()  
                break
        except Exception:
            pass


def main_cycle():
    print("🎧 Waiting for your command...")
    query = takeCommand()
    if query != "none":
        executeCommand(query)
    else:
        speak("I didn’t catch that. Try again.")
        main_cycle()
    sleep_and_listen()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

if __name__ == "__main__":
    wishMe()
    speak("Im Assistant. How can I help you?")
    main_cycle()

