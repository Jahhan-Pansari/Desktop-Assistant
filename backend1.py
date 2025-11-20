import os
import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

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

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendMail(to, content):
    from email.message import EmailMessage
    import ssl
    import smtplib

    email_sender = 's.jahhan.pansari@fountainheadschools.org'
    email_password = 'lufrurrprhrbnojs'  # Consider securing this better
    email_receiver = to
    subject = "Email for you"
    body = content

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("My name is Jarvis. How can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User  said: {query}")
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that. Please try again.")
        return "None"
    except sr.RequestError:
        print("Could not request results; check your network connection.")
        return "None"
    return query.lower()

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

    # Format the mail into a Gmail compose link
    mail_url = (
        f"https://mail.google.com/mail/?view=cm&fs=1"
        f"&to={to}"
        f"&su={subject.replace(' ', '%20')}"
        f"&body={body.replace(' ', '%20')}"
    )

    speak(f"Opening Gmail to send your mail to {recipient_name}.")
    webbrowser.open(mail_url)

def main():
    wishMe()
    while True:
        query = takeCommand()
        if query == "none":
            continue

        if 'quit' in query or 'bye' in query:
            speak("Quitting program, thank you for using.")
            break

        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                print(e)
                speak("Sorry, I couldn't find any results.")

        elif 'gmail' in query:
            speak("Opening Gmail")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif 'open file manager' in query:
            filemanagerpath = "C:\\Windows\\explorer.exe"
            os.startfile(filemanagerpath)

        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open_new_tab("https://www.youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif 'open wikipedia' in query:
            speak("Opening Wikipedia")
            webbrowser.open_new_tab("https://en.wikipedia.org/")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open car for sale' in query:
            carforsale_path = ("C:\\Users\\Admin\\Downloads\\Car.for.Sale.Simulator.2023.v0.2.3\\"
                               "Car.for.Sale.Simulator.2023.v0.2.3\\Car.for.Sale.Simulator.2023.v0.2.3\\"
                               "Car For Sale Simulator 2023.exe")
            speak("Opening Car For Sale Simulator")
            os.startfile(carforsale_path)

        elif 'open blender' in query:
            blender_path = "E:\\Blender\\blender-4.1....11-windows-x64\\blender.exe"
            speak("Opening Blender")
            os.startfile(blender_path)

        elif 'open chrome' in query:
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            speak("Opening Chrome Browser")
            os.startfile(chrome_path)

        elif 'what is my name' in query:
            speak("Your name is Jahhan Pansari")

        elif 'send a mail' in query:
            compose_mail()

if __name__ == "__main__":
    main()
