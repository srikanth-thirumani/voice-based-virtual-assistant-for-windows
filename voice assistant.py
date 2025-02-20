import subprocess
import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import time
import datetime
import smtplib
import requests
import psutil
import socket
import re
from datetime import datetime
import cv2
from dotenv import load_dotenv
from PIL import Image
import io
import speedtest
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
import pywhatkit
import pyautogui
import datetime
import google.generativeai as genai
from typing import Optional


load_dotenv()
DREAMSTUDIO_API = os.getenv('DREAMSTUDIO_API')
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

recognizer = sr.Recognizer()
mic = sr.Microphone()

command_keywords = {
    'shutdown': ['shutdown', 'power down', 'turn off'],
    'open chrome': ['chrome', 'google chrome', 'open chrome'],
    'open edge': ['edge', 'microsoft edge', 'open edge'],
    'open store': ['store', 'microsoft store', 'open store'],
    'open linkedin': ['linkedin', 'open linkedin','open linkedIn','linkedIn'],
    'open file manager': ['file manager', 'explorer', 'open file manager'],
    'open vs code': ['visual studio code', 'vs code', 'open vs code'],
    'open youtube': ['youtube', 'open youtube'],
    'google search': ['google', 'search', 'search google'],
    'play music on youtube': ['music', 'play music', 'youtube music'],
    'what time is it': ['time', 'current time', 'what time'],
    'make a phone call': ['phone call', 'call', 'make a call'],
    'send email': ['email', 'send email'],
    'search youtube': ['search youtube', 'on youtube'],
    'make a note': ['note', 'make a note', 'write down'],
    'weather': ['weather', 'what is the weather'],
    'reminder': ['reminder', 'set a reminder'],
    'joke': ['joke', 'tell me a joke'],
    'system info': ['system info', 'system information'],
    'movies':['trending movies','movies','popular movies'],
    'news': ['news', 'latest news','current news'],
    'calendar': ['calendar', 'check calendar'],
    'check IP address': ['ip address', 'check ip', 'what is my ip', 'check IP address', 'IP address'],
    'navigate': ['navigate', 'directions', 'navigate to'],
    'open camera': ['camera', 'open camera', 'start camera'],
    'speed test': ['speedtest', 'network speed', 'check speed', 'speed test', 'check the internet speed','check internet speed'],

    'whatsapp message': ['send whatsapp message', 'whatsapp', 'message on whatsapp', 'whatsapp message', 'send message on whatsapp', 'send message  to', 'whatsapp to', 'message someone on whatsapp', 'send a whatsapp', 'send a message to',"sena a whatsapp message"],

'screenshot': ['screenshot', 'take screenshot', 'capture screen', 'screen capture', 'save screenshot', 'take a picture of screen', 'capture display','take a screenshot'],


    'generate image': ['generate image', 'create image','create a picture','make picture', 'generate a picture']
}


def listen_for_wake_word():
    with mic as source:
        print("Listening for wake word...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        wake_word = recognizer.recognize_google(audio, language='en-IN').lower()
        print(f"Recognized wake word: {wake_word}")
        if wake_word in ["hi windows", "hello windows", "hey windows","srikanth"]:
            speak("Yes, how can I assist you?")
            return True
        else:
            print("Wake word not recognized correctly.")
            return False
    except sr.UnknownValueError:
        print("Didn't recognize the wake word.")
    except sr.RequestError as e:
        print(f"Request error: {e}")

    return False

def listen_and_respond():
    with mic as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening for your command...")
        audio = recognizer.listen(source)
        print("Recording complete.")

    try:
        print("Recognizing speech...")
        command = recognizer.recognize_google(audio, language='en-IN')
        print(f"Recognized command: {command}")
        speak(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        error_message = "I didn't quite catch that. Please repeat."
        print(error_message)
        speak(error_message)
        return ""
    except sr.RequestError as e:
        error_message = f"Request error: {e}"
        print(error_message)
        speak(error_message)
        return ""
def ask_if_more_tasks():
    speak("Is there any other task to do?")
    response = listen_and_respond()
    if 'yes' in response or 'ok' in response or 'continue' in response or 'proceed' in response:
        return True
    else:
        speak("Okay, I'll wait for your next command.")
        return False
def shutdown_computer():
    speak("Shutting down the computer.")
    subprocess.call(["shutdown", "/s", "/t", "1"])
def search_youtube(query):
    speak(f"Searching for {query} on YouTube")
    pywhatkit.playonyt(query)
def open_application(app_name):
    if app_name == 'chrome':
        webbrowser.open("https://www.google.com/chrome/")
    elif app_name == 'edge':
        webbrowser.open("https://www.microsoft.com/edge")
    elif app_name == 'store':
        os.system("start ms-windows-store:")
    elif app_name == 'file manager':
        os.system("explorer")
    elif app_name == 'vs code':
        subprocess.Popen(["code"])
    elif app_name == 'youtube':
        webbrowser.open("https://www.youtube.com")
    else:
        speak("Application not recognized.")

def search_google(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)
def youtube(query):
    search_url = f"https://www.youtube.com/results?search_query={query}"
    speak(f"Searching for {query} on YouTube")
    webbrowser.open(search_url)
def send_whatsapp_message(phone_number, message):
    # You can either schedule the message or send it instantly
    try:
        speak(f"Sending WhatsApp message to {phone_number}.")

        # Get current time
        current_time = datetime.datetime.now()
        hour = current_time.hour
        minute = current_time.minute + 1  # Schedule 1 minute later to allow time for execution

        # Scheduled message (sent at the specified time)
        #pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
        #speak("WhatsApp message scheduled successfully.")

        # If you want to send instantly, you can use:
        pywhatkit.sendwhatmsg_instantly(phone_number, message)
        speak("WhatsApp message sent instantly.")

    except Exception as e:
        print(f"Failed to send WhatsApp message: {e}")
        speak(f"Failed to send WhatsApp message: {e}")

def whatsapp_handler():
    speak("Please provide the contact number.")
    phone_number = listen_and_respond()

    if phone_number:
        phone_number = re.sub(r'\D', '', phone_number)  # Remove non-numeric characters
        if phone_number:
            speak("What message would you like to send?")
            message = listen_and_respond()

            if message:
                # Call the function to send the message
                send_whatsapp_message(f"+91{phone_number}", message)
            else:
                speak("No message provided.")
        else:
            speak("No valid phone number provided.")
    else:
        speak("Phone number not recognized.")

def tell_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    time_message = f"The current time is {current_time}."
    print(time_message)
    speak(time_message)


def send_email():
    try:
        # Ask for the recipient's email address through the keyboard
        to = input("Enter recipient's email address: ")

        # Ask for the subject of the email through voice command
        speak("What is the subject of the email?")
        subject = listen_and_respond()

        # Ask for the body of the email through voice command
        speak("What would you like the email to say?")
        body = listen_and_respond()

        # Email content format
        content = f"Subject: {subject}\n\n{body}"

        # Email credentials (You must replace with your own email and password)
        email = 'srikanththirumani01@gmail.com'
        password = 'qeqc jnok ymzy jxpt'

        # Setting up the email server and sending the email
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, to, content)
        server.quit()

        # Confirm that the email was sent
        speak("Email sent successfully.")

    except Exception as e:
        speak(f"Failed to send email: {e}")

def make_a_note():
    speak("What would you like to note down?")
    note = listen_and_respond()
    if note:
        # Store the note (e.g., in a file or a database)
        speak(f"Note added: {note}")

def get_weather(city):
    api_key = 'd82f8b316fde1b6a5618f2bf0c3fabb6'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    if response['cod'] == 200:
        weather = response['weather'][0]['description']
        temperature = response['main']['temp']
        weather_info = f"The weather in {city} is currently {weather} with a temperature of {temperature} degrees Celsius."
        print(weather_info)  # Display on screen
        speak(weather_info)  # Speak the information
    else:
        error_message = "I couldn't fetch the weather information."
        print(error_message)
        speak(error_message)
def make_phone_call(contact_name):
    speak("Please provide the phone number or contact.")
    phone_number = listen_and_respond()

    if phone_number:
        phone_number = re.sub(r'\D', '', phone_number)  # Remove non-numeric characters
        if phone_number:
            url = f"tel:{phone_number}"
            try:
                subprocess.Popen(["ms-settings:phone"], shell=True)
                speak(f"Dialing {phone_number}.")
                webbrowser.open(url)
            except Exception as e:
                speak(f"Failed to make a phone call: {e}")
        else:
            speak("No valid phone number provided.")
    else:
        speak("Phone number or contact name not recognized.")
def set_reminder(reminder_time, message):
    # Convert reminder_time to a datetime object and set up the reminder (mockup)
    speak(f"Reminder set for {reminder_time} with message: {message}")

def tell_joke():
    joke = "Why don't scientists trust atoms? Because they make up everything!"
    speak(joke)
    print(joke)

def system_info():
    cpu_usage = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')

    system_info_message = (f"CPU Usage: {cpu_usage}%\n"
                           f"Memory Usage: {memory_info.percent}%\n"
                           f"Disk Usage: {disk_info.percent}%")
    speak(system_info_message)
    print(system_info_message)

def fetch_news():
    api_key = 'a2f3b0f44494419494c1dbada5e1dc51'
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url).json()
    if response['status'] == 'ok':
        articles = response['articles'][:3]
        news_titles = [article['title'] for article in articles]
        news_info = "Here are the top news headlines:"
        print(news_info)
        speak(news_info)
        for title in news_titles:
            print(title)
            speak(title)
    else:
        error_message = "I couldn't fetch the news."
        print(error_message)
        speak(error_message)

def check_calendar():
    # Replace this with actual calendar checking logic
    speak("Checking your calendar...")
def navigate_to_city(city_name):
    if city_name:
        maps_url = f"https://www.google.com/maps/dir/?api=1&destination={city_name.replace(' ', '+')}"
        speak(f"Navigating to {city_name}.")
        webbrowser.open(maps_url)
    else:
        speak("I couldn't recognize the city name. Please try again.")
def open_camera():
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        speak("Camera not found.")
        return
    speak("Opening camera.")
    while True:
        ret, frame = camera.read()
        if not ret:
            break
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    camera.release()
    cv2.destroyAllWindows()
def get_popular_movies():
    try:
        # Replace 'YOUR_API_KEY' with your actual OMDb API key
        OMDB_API_KEY = '4161ed01'
        current_year = datetime.date.today().year

        # Make request to OMDb API
        response = requests.get(
            f"http://www.omdbapi.com/?s=popular&y={current_year}&apikey={OMDB_API_KEY}"
        ).json()

        # Check if the response contains movies
        if 'Search' in response:
            print()
            for movie in response["Search"]:
                title = movie.get('Title', 'No Title Available')
                print(title)
        else:
            print("No movies found or error occurred.")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
    except KeyError:
        print("Error parsing response.")
        return None
import datetime as t
def screenshot() -> None:
    try:
        img = pyautogui.screenshot()
        # Add timestamp to the filename to avoid overwriting
        timestamp = t.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        img_dir = r"C:\Users\srika\OneDrive\Desktop\Documents\mini project"
        if not os.path.exists(img_dir):
            os.makedirs(img_dir)  # Ensure the directory exists
        img_path = os.path.join(img_dir, f"ss_{timestamp}.png")
        img.save(img_path)
        print(f"Screenshot saved at {img_path}")
    except Exception as e:
        print(f"An error occurred while taking the screenshot: {e}")


import speedtest  # Make sure to use: pip install speedtest-cli

def test_speed():
    """
    Test internet speed using a simple download method
    """
    # URL of a known large file for testing download speed
    url = "https://speed.cloudflare.com/__down?bytes=25000000"  # 25MB file from Cloudflare
    
    try:
        speak("Testing your internet speed. This will take a few moments...")
        print("Starting speed test...")
        
        # Test download speed
        print("Testing download speed...")
        start_time = time.time()
        response = requests.get(url, stream=True)
        size = 0
        
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                size += len(chunk)
        
        end_time = time.time()
        duration = end_time - start_time
        
        # Calculate speed in Mbps
        speed_bps = (size * 8) / duration
        speed_mbps = speed_bps / 1_000_000
        
        # Test latency (ping)
        print("Testing ping...")
        ping_start = time.time()
        requests.get('http://www.google.com')
        ping = (time.time() - ping_start) * 1000  # Convert to ms
        
        # Format results
        speed_message = (
            f"Here are your internet speed test results:\n"
            f"Download speed: {speed_mbps:.2f} Mbps\n"
            f"Latency (Ping): {ping:.0f} ms"
        )
        
        print(speed_message)
        speak(speed_message)
        
    except requests.RequestException as e:
        error_message = f"Sorry, I encountered an error while testing your internet speed: {str(e)}"
        print(error_message)
        speak(error_message)
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        print(error_message)
        speak(error_message)
def setup_gemini():
    """
    Initialize the Gemini API with your API key
    """
    GOOGLE_API_KEY ="AIzaSyDot8VOtEx6PFIDTN7JBBuVgg-sznlqiMM"  # Add this to your .env file
    genai.configure(api_key=GOOGLE_API_KEY)
    
    # Set up the model
    model = genai.GenerativeModel('gemini-pro')
    return model

def get_ai_response(command: str, model: Optional[genai.GenerativeModel] = None) -> str:
    """
    Gets an AI response using Gemini API for commands that don't match predefined keywords.
    
    Args:
        command (str): The user's command/question
        model (GenerativeModel): Optional pre-configured Gemini model instance
    
    Returns:
        str: AI-generated response
    """
    try:
        if model is None:
            model = setup_gemini()
        
        # Create a prompt that guides Gemini to provide a helpful response
        prompt = f"""
        You are a helpful AI assistant. Please provide a clear and concise response to the following query:
        {command}
        
        Respond in a natural, conversational way. If the query is unclear, ask for clarification.
        Keep the response short and to the point and if any mistake in command correct it.
        """
        
        # Generate response
        response = model.generate_content(prompt)
        
        # Extract and clean the response text
        if response.text:
            return response.text.strip()
        else:
            return "I apologize, but I couldn't generate a response for that query. Could you please rephrase it?"
            
    except Exception as e:
        print(f"Error generating AI response: {e}")
        return "I apologize, but I'm having trouble generating a response right now. Please try again later."


def get_ip(_return=False):
    try:
        response = requests.get(f'http://ip-api.com/json/').json()
        if _return:
            return response
        else:
            return f'Your IP address is {response["query"]}'
    except KeyboardInterrupt:
        return None
    except requests.exceptions.RequestException:
        return None
    
def open_linkedin():
    speak("Opening LinkedIn")
    webbrowser.open("https://www.linkedin.com")

def generate_image(text):
    # Initialize the Stability API client
    stability_api = client.StabilityInference(
        key=DREAMSTUDIO_API,
        verbose=True,
    )

    # Generate image based on the prompt text
    answers = stability_api.generate(
        prompt=text,
        seed=95456,
    )

    # Process the API response and handle the image
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                print("WARNING: Your request activated the API's safety filters and could not be processed."
                      "Please modify the prompt and try again.")
                speak("Your request was filtered. Please try with a different prompt.")
                return
            elif artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary))
                img.show()
                speak("Here is the image I generated based on your description.")

def handle_command(command: str, model: Optional[genai.GenerativeModel] = None) -> None:
    """
    Handle user commands with Gemini AI fallback
    
    Args:
        command (str): The user's command
        model (Optional[GenerativeModel]): Pre-configured Gemini model instance
    """
    # First, check for known commands
    command_matched = False
    
    # Check if command matches 'play music' or similar
    if any(keyword in command for keyword in command_keywords['play music on youtube']):
        search_youtube(command.replace('play', '').strip())
        command_matched = True
    elif any(keyword in command for keyword in command_keywords['shutdown']):
        shutdown_computer()
        command_matched = True
    elif any(keyword in command for keyword in command_keywords['open chrome']):
        open_application('chrome')
        command_matched = True
    elif any(keyword in command for keyword in command_keywords['open edge']):
        open_application('edge')
        command_matched = True
    elif any(keyword in command for keyword in command_keywords['open store']):
        open_application('store')
        command_matched = True
    elif any(keyword in command for keyword in command_keywords['open file manager']):
        open_application('file manager')
        command_matched = True
    elif any(keyword in command for keyword in command_keywords['open linkedin']):
        open_linkedin()
        command_matched = True
    elif any(keyword in command for keyword in command_keywords['open youtube']):
        open_application('youtube')
        command_matched = True
    elif any(keyword in command for keyword in command_keywords['google search']):
        query = command.replace('search', '').replace('on google', '').strip()
        search_google(query)
        command_matched = True
    elif any(keyword in command for keyword in command_keywords['search youtube']):
        query = command.replace('search', '').replace('on youtube', '').strip()
        youtube(query)
        command_matched = True
    elif any(keyword in command for keyword in command_keywords['screenshot']):
        screenshot()
        command_matched = True
    elif any(keyword in command for keyword in command_keywords['what time is it']):
        tell_time()
        command_matched = True
    elif any(keyword in command for keyword in command_keywords['check IP address']):
        ip = get_ip()
        if ip:
            print(ip)
            speak(ip)
        command_matched = True
    elif any(keyword in command for keyword in command_keywords['make a phone call']):
        make_phone_call("Contact")
        command_matched = True
    elif any(keyword in command for keyword in command_keywords['movies']):
        speak("Some of the latest popular movies are as follows:")
        get_popular_movies()
        command_matched = True
    elif any(keyword in command for keyword in command_keywords['send email']):
        send_email()
        command_matched = True
    elif any(keyword in command for keyword in command_keywords['make a note']):
        make_a_note()
        command_matched = True
    elif any(keyword in command for keyword in command_keywords['weather']):
        city = command.replace('check the weather in', '').strip()
        get_weather(city)
        command_matched = True
    elif any(keyword in command for keyword in command_keywords['reminder']):
        reminder_time = "5 PM"  # Extract this from the command
        message = re.sub('reminder', '', command).strip()
        set_reminder(reminder_time, message)
        command_matched = True
    elif any(keyword in command for keyword in command_keywords['joke']):
        tell_joke()
        command_matched = True
    elif any(keyword in command for keyword in command_keywords['system info']):
        system_info()
        command_matched = True
    elif any(keyword in command for keyword in command_keywords['news']):
        fetch_news()
        command_matched = True
    elif any(keyword in command for keyword in command_keywords['calendar']):
        check_calendar()
        command_matched = True
    elif any(keyword in command for keyword in command_keywords['open camera']):
        open_camera()
        command_matched = True
    elif any(keyword in command for keyword in command_keywords['whatsapp message']):
        whatsapp_handler()
        command_matched = True
    elif any(keyword in command for keyword in command_keywords['speed test']):
        test_speed()
        command_matched = True
    elif any(keyword in command for keyword in command_keywords['navigate']):
        city_name = command.replace('navigate to', '').strip()
        result = navigate_to_city(city_name)
        print(result)
        command_matched = True
    elif any(keyword in command for keyword in command_keywords['generate image']):
        speak("What would you like the image to be about?")
        image_description = listen_and_respond()
        if image_description:
            generate_image(image_description)
        else:
            speak("Sorry, I didn't catch that.")
        command_matched = True
    
    # If no command matched, use Gemini AI response
    if not command_matched:
        ai_response = get_ai_response(command, model)
        print(ai_response)
        speak(ai_response)

def main():
    # Initialize Gemini model once at startup
    try:
        model = setup_gemini()
    except Exception as e:
        print(f"Error initializing Gemini AI: {e}")
        model = None
    
    while True:
        if listen_for_wake_word():
            keep_listening = True
            while keep_listening:
                command = listen_and_respond()
                if not command:
                    continue
                
                # Handle the command with fallback to Gemini AI response
                handle_command(command, model)
                keep_listening = ask_if_more_tasks()

if __name__ == "__main__":
    main()