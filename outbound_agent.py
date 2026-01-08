import os
import smtplib
import time
import random
from email.message import EmailMessage
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

def send_pitch_email(recipient_email, business_name, pitch_content):
    msg = EmailMessage()
    msg.set_content(pitch_content)
    msg['Subject'] = f"AI Efficiency Audit: {business_name}"
    msg['From'] = os.getenv("GMAIL_USER")
    msg['To'] = recipient_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(os.getenv("GMAIL_USER"), os.getenv("GMAIL_APP_PASSWORD"))
            smtp.send_message(msg)
        return True
    except Exception as e:
        print(f"Failed to send to {business_name}: {e}")
        return False

def generate_pitch(lead):
    # If name is missing or generic, use a natural greeting
    contact = lead.get('contact_name', '')
    greeting = f"Hi {contact}," if contact and contact != "N/A" else "Hi there,"
    
    location = lead.get('location', 'the 806') # Default to 806 if location is empty

    prompt = f"""
    Write a short, 3-sentence email. 
    Tone: Professional, local, helpful. No metaphors.
    
    Context: I'm a developer in {location}.
    Greeting: {greeting}
    Business: {lead['name']}
    Problem to solve: {lead['gap']}
    
    Closing: "I'm right here in town—can I send you a quick video of how this works?"
    """
    # ... rest of your OpenAI call ...    return response.choices[0].message.content

# --- THE AUTOMATED PURSUIT ---
# Using the enriched data from your Lubbock Analysis
leads = [
    {"name": "Raider West Designs", "email": "test1@yourdomain.com", "ind": "Plumbing"},
    {"name": "Hart Heating & AC", "email": "test2@yourdomain.com", "ind": "HVAC"},
    # Add your other leads here
]

print(f"Starting pursuit of {len(leads)} leads...")

for lead in leads:
    print(f"\n--- Processing: {lead['name']} ---")
    
    # 1. Generate unique pitch
    pitch = generate_pitch(lead['name'], lead['ind'])
    
    # 2. Send the email
    success = send_pitch_email(lead['email'], lead['name'], pitch)
    
    if success:
        print(f"SUCCESS: Pitch delivered to {lead['name']}.")
        
        # 3. THE THROTTLE (The most important part)
        wait_time = random.randint(45, 90) # Random gap between 45 and 90 seconds
        print(f"Mimicking human behavior... Waiting {wait_time}s before next lead.")
        time.sleep(wait_time)

print("\nAll leads processed. Pursuit sequence complete.")
import os
from dotenv import load_dotenv

load_dotenv()

print(f"Checking Email: {os.getenv('GMAIL_USER')}")
print(f"Checking OpenAI Key: {'Found' if os.getenv('OPENAI_API_KEY') else 'MISSING'}")
