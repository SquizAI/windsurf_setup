#!/usr/bin/env python3
import smtplib
import time
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
            if '=' in line:
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
ADMIN_EMAIL = env_vars.get('ADMIN_EMAIL', 'mattystjh@gmail.com')

# Load HTML email content
with open('email_to_students.html', 'r') as file:
    html_content = file.read()

# Also create a plain text version for email clients that don't support HTML
plain_text_content = """
VibeCode 101 - Accessing Your Windsurf Setup Guide & Resources

Dear VibeCode 101 Students,

I hope this email finds you well. I'm writing to share important information about accessing the Windsurf setup guide and resources we've created for this course.

GitHub Repository Access: https://github.com/SquizAI/windsurf_setup

Please follow the instructions in the repository to install and set up Windsurf for our upcoming classes.

Best regards,
Matty Squarzoni
VibeCode 101 Instructor
mattystjh@gmail.com
"""

email_subject = "VibeCode 101 - Accessing Your Windsurf Setup Guide"

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

# Connect to email server
try:
    if EMAIL_SECURE:
        server = smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT)
    else:
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
    
    server.login(EMAIL_USER, EMAIL_PASS)
    print(f"Connected to email server: {EMAIL_HOST}:{EMAIL_PORT}")
except Exception as e:
    print(f"Error connecting to email server: {e}")
    sys.exit(1)

# Send individual emails
successful = 0
failed = 0

for i, student_email in enumerate(students):
    try:
        # Create message
        msg = MIMEMultipart("alternative")
        msg["Subject"] = email_subject
        msg["From"] = formataddr(("VibeCode 101", EMAIL_USER))
        msg["To"] = student_email
        msg["Cc"] = ADMIN_EMAIL
        
        # Attach plain text and HTML content
        part1 = MIMEText(plain_text_content, "plain")
        part2 = MIMEText(html_content, "html")
        
        # Add parts in order: plain text version first, then HTML version
        msg.attach(part1)
        msg.attach(part2)
        
        # Calculate all recipients (both To and Cc)
        all_recipients = [student_email]
        if student_email.lower() != ADMIN_EMAIL.lower():  # Avoid duplicate if student is also admin
            all_recipients.append(ADMIN_EMAIL)
        
        print(f"Sending HTML email {i+1}/{len(students)} to: {student_email}")
        server.send_message(msg, from_addr=EMAIL_USER, to_addrs=all_recipients)
        
        print(f"  ✓ Sent successfully")
        successful += 1
        
        # Wait 3 seconds before sending the next email
        if i < len(students) - 1:
            print(f"  Waiting 3 seconds before sending next email...")
            time.sleep(3)
            
    except Exception as e:
        print(f"  ✗ Error sending to {student_email}: {e}")
        failed += 1

# Close the connection
server.quit()
print("\nEmail sending completed!")
print(f"Successful: {successful} | Failed: {failed} | Total: {len(students)}")
print(f"All emails were CC'd to: {ADMIN_EMAIL}")
print(f"Emails were sent in HTML format with a plain text fallback")
