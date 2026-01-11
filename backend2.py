import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import requests
import urllib.parse
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

emaildetailsDict = {
    "vedant": "s.vedant.dhameliya@fountainheadschools.org",
    "shashank sir": "s.shashank.ray@fountainheadschools.org",
    "tejas sir": "s.tejas.gamit@fountainheadschools.org",
    "dhairya": "s.dhairya.garg@fountainheadschools.org",
    "pankaj": "pansaripankaj@gmail.com",
    "parents of jahhan": "p.jahhan.pansari@fountainheadschools.org",
    "self": "s.jahhan.pansari@fountainheadschools.org",
}

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand(timeout=5, phrase_time_limit=7):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙 Listening...")
        try:
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query.lower()
        except Exception:
            return None

def compose_mail():
    speak("Who would you like to send the mail to?")
    name = takeCommand()
    if not name:
        speak("I didn't catch that.")
        return

    to = emaildetailsDict.get(name)
    if not to:
        speak("I couldn't find that contact.")
        return

    speak("What is the subject?")
    subject = takeCommand() or ""

    speak("What should I write?")
    body = takeCommand() or ""

    mail_url = (
        "https://mail.google.com/mail/?view=cm&fs=1"
        f"&to={urllib.parse.quote(to)}"
        f"&su={urllib.parse.quote(subject)}"
        f"&body={urllib.parse.quote(body)}"
    )

    speak("Opening Gmail.")
    webbrowser.open(mail_url)

def open_application(query):
    from groq import Groq

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Return only the correct website URL. No extra text."},
            {"role": "user", "content": query}
        ]
    )

    url = response.choices[0].message.content.strip()
    webbrowser.open(url)

def executeCommand(query):
    if "send a mail" in query:
        compose_mail()

    elif any(word in query for word in ["open", "start", "launch", "play"]):
        open_application(query)

    elif "time" in query:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")

    else:
        speak("I did not understand. This is what I found online.")
        open_application(query)

def assistant_loop():
    while True:
        query = takeCommand()
        if not query:
            continue

        if query in ["assistant quit", "bye assistant", "exit assistant"]:
            speak("Goodbye.")
            break

        executeCommand(query)

def wishMe():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning")
    elif hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")

#compile n run
if __name__ == "__main__":
    wishMe()
    speak("I am Assistant. How can I help you?")
    assistant_loop()
