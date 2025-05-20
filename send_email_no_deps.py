#!/usr/bin/env python3
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
import sys

# Parse .env file manually
def load_env_file(env_path):
    env_vars = {}
    with open(env_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            key, value = line.split('=', 1)
            env_vars[key] = value
    return env_vars

# Load environment variables
env_path = '.env'
env_vars = load_env_file(env_path)

# Email configuration from .env file
EMAIL_HOST = env_vars.get('EMAIL_HOST')
EMAIL_PORT = int(env_vars.get('EMAIL_PORT', '465'))
EMAIL_USER = env_vars.get('EMAIL_USER')
EMAIL_PASS = env_vars.get('EMAIL_PASS')
EMAIL_SECURE = env_vars.get('EMAIL_SECURE', 'true').lower() == 'true'
ADMIN_EMAIL = env_vars.get('ADMIN_EMAIL')

# Verify if we have all required environment variables
missing_vars = []
for var_name in ['EMAIL_HOST', 'EMAIL_PORT', 'EMAIL_USER', 'EMAIL_PASS']:
    if not env_vars.get(var_name):
        missing_vars.append(var_name)

if missing_vars:
    print(f"Error: Missing required environment variables: {', '.join(missing_vars)}")
    print("Please make sure your .env file contains all required variables.")
    sys.exit(1)

# Load email content
with open('email_to_students.md', 'r') as file:
    email_content = file.read()
    email_subject = "VibeCode 101 - Accessing Your Windsurf Setup Guide & Resources"

# Student email addresses
students = [
    "patrick.scott003@mymdc.net",
    "jazminevendorra@gmail.com",
    "dlv.work.0@gmail.com",
    "teslitup@gmail.com",
    "pmu@taviragroup.com",
    "jmefitinfo@gmail.com",
    "usmctbone2@gmail.com",
    "noelle@noelle.ai",
    "con.tech.johnson@gmail.com",
    "gkarelitz@gmail.com",
    "mmannino@mdc.edu",
    "mattystjh@gmail.com",
    "gianmariatroiani@gmail.com",
    "am.rubins@gmail.com",
    "cscastilloliva90@gmail.com",
    "mariaj.tellez95@gmail.com",
    "david.joseph013@mymdc.net",
    "raque.quintanilla002@mymdc.com"
]

def send_email():
    # Create message
    msg = MIMEMultipart()
    msg["Subject"] = email_subject
    msg["From"] = formataddr(("VibeCode 101", EMAIL_USER))
    msg["Reply-To"] = ADMIN_EMAIL
    msg["Bcc"] = ", ".join(students)  # Using BCC for privacy
    
    # Attach plain text content
    part = MIMEText(email_content, "plain")
    msg.attach(part)
    
    print(f"\nPreparing to send email to {len(students)} students...")
    print(f"Using email server: {EMAIL_HOST}:{EMAIL_PORT}")
    print(f"Sending from: {EMAIL_USER}")
    
    try:
        # Connect to server and send email
        if EMAIL_SECURE:
            server = smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT)
        else:
            server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
            server.starttls()  # Secure the connection
            
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)
        server.quit()
        print(f"Email successfully sent to {len(students)} students!")
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        print("\nTroubleshooting:")
        print("- Check your server connection")
        print("- Verify credentials in .env file")
        print("- Ensure your email provider allows SMTP access")
        return False

if __name__ == "__main__":
    print("Windsurf Setup Guide - Email Sender")
    print("===================================")
    print("This script will send the Windsurf Setup Guide email to all students.")
    print("Using credentials from .env file.\n")
    
    proceed = input("Do you want to proceed with sending the email? (y/n): ")
    if proceed.lower() == 'y':
        send_email()
    else:
        print("Email sending cancelled.")
