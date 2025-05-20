#!/usr/bin/env python3
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
import dotenv
import sys

# Load environment variables
dotenv.load_dotenv()

# Email configuration from .env file
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 465))
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')
EMAIL_SECURE = os.getenv('EMAIL_SECURE', 'true').lower() == 'true'
ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')

# Verify if we have all required environment variables
missing_vars = []
for var_name in ['EMAIL_HOST', 'EMAIL_PORT', 'EMAIL_USER', 'EMAIL_PASS']:
    if not os.getenv(var_name):
        missing_vars.append(var_name)

if missing_vars:
    print(f"Error: Missing required environment variables: {', '.join(missing_vars)}")
    print("Please make sure your .env file contains all required variables.")
    sys.exit(1)

# Email content
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
    except Exception as e:
        print(f"Error sending email: {e}")
        print("\nTroubleshooting:")
        print("- Check your server connection")
        print("- Verify credentials in .env file")
        print("- Ensure your email provider allows SMTP access")
        print("- If using Gmail, make sure to use an App Password")

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
