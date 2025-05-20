#!/usr/bin/env python3
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass

# Email content (plain text for simplicity)
email_subject = "VibeCode 101 - Accessing Your Windsurf Setup Guide & Resources"
email_body = """
Dear VibeCode 101 Students,

I hope this email finds you well. I'm writing to share important information about accessing the Windsurf setup guide and resources we've created for this course. These materials will help you get started with Windsurf, an advanced AI-powered IDE that we'll be using throughout our program.

## GitHub Repository Access

We've created a comprehensive guide and reference materials, all available through our GitHub repository. Here's how to access and use it:

1. Repository URL: https://github.com/SquizAI/windsurf_setup

2. Accessing the Repository:
   - Simply click on the link above to view the repository in your web browser
   - No GitHub account is required to view and download the materials
   - If you have a GitHub account, you can "star" the repository to easily find it later

3. Repository Contents:
   - A detailed markdown guide covering Windsurf installation for all platforms
   - Step-by-step setup instructions
   - Introduction to Cascade (Windsurf's AI assistant)
   - MCP (Model Context Protocol) functionality guide
   - Troubleshooting tips
   - 8-lesson curriculum for beginners (approximately 13 hours)
   - Additional resources and references

4. Downloading the Files:
   - To download all files at once, click the green "Code" button and select "Download ZIP"
   - Individual files can be viewed and downloaded by clicking on them in the repository

## Why This Matters

Windsurf is a cutting-edge AI IDE that will significantly enhance your coding productivity and learning experience. The guide we've created will help you install and set up Windsurf properly, understand its key features, and learn how to leverage its AI capabilities effectively.

## Next Steps

1. Access the repository using the link above
2. Follow the installation instructions for your specific operating system
3. Complete the setup process
4. Work through the beginner lessons at your own pace
5. Come to our next class with Windsurf installed and ready to use

If you encounter any issues accessing the repository or setting up Windsurf, please don't hesitate to reach out to me directly. I'm here to help ensure everyone is properly set up and ready for our upcoming sessions.

Looking forward to seeing you all in our next class!

Best regards,
Matty Squarzoni
VibeCode 101 Instructor
mattystjh@gmail.com
"""

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
    msg = MIMEMultipart()
    msg["Subject"] = email_subject
    msg["From"] = sender_email
    msg["Bcc"] = ", ".join(students)  # Using BCC for privacy
    
    # Attach plain text content
    part = MIMEText(email_body, "plain")
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
