#!/usr/bin/env python3
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import markdown
import getpass

# Email content from markdown file
with open('email_to_students.md', 'r') as file:
    content = file.read()
    # Extract subject from the markdown content
    subject_line = content.split('**Subject:')[1].split('**')[0].strip()
    # Convert markdown to HTML for email
    html_content = markdown.markdown(content)

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
    sender_email = input("Enter your email address: ")
    password = getpass.getpass("Enter your email password (input will be hidden): ")
    
    # Determine SMTP server based on email domain
    smtp_server = ""
    smtp_port = 587
    if "gmail" in sender_email.lower():
        smtp_server = "smtp.gmail.com"
    elif "outlook" in sender_email.lower() or "hotmail" in sender_email.lower():
        smtp_server = "smtp-mail.outlook.com"
    elif "yahoo" in sender_email.lower():
        smtp_server = "smtp.mail.yahoo.com"
    else:
        smtp_server = input("Enter your SMTP server (e.g., smtp.gmail.com): ")
        smtp_port = int(input("Enter your SMTP port (default 587): ") or "587")
    
    # Create message
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject_line
    msg["From"] = sender_email
    msg["Bcc"] = ", ".join(students)  # Using BCC for privacy
    
    # Attach HTML content
    part = MIMEText(html_content, "html")
    msg.attach(part)
    
    print(f"\nPreparing to send email to {len(students)} students...")
    
    try:
        # Connect to server and send email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(sender_email, password)
        server.send_message(msg)
        server.quit()
        print(f"Email successfully sent to {len(students)} students!")
    except Exception as e:
        print(f"Error sending email: {e}")
        
        if "gmail" in sender_email.lower():
            print("\nFor Gmail users:")
            print("1. Make sure you have 2FA enabled on your Google account")
            print("2. Create an App Password at https://myaccount.google.com/apppasswords")
            print("3. Use that App Password instead of your regular password")
        
        print("\nGeneral troubleshooting:")
        print("- Check your email address and password")
        print("- Verify SMTP server and port")
        print("- Ensure your email provider allows SMTP access")

if __name__ == "__main__":
    print("Windsurf Setup Guide - Email Sender")
    print("===================================")
    print("This script will send the Windsurf Setup Guide email to all students.")
    print("You'll need to provide your email credentials to send the message.\n")
    
    proceed = input("Do you want to proceed? (y/n): ")
    if proceed.lower() == 'y':
        send_email()
    else:
        print("Email sending cancelled.")
