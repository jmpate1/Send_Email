import smtplib
import ssl
from email.message import EmailMessage

subject = "Email from Python"
body = "This is a test email from Python"
sender_email = "pate.jason.m@gmail.com"
receiver_email = "pate.jason.m@gmail.com"
password = input("Enter password now: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

#This no longer works because Google has updated their policy regarding less secure apps
print("Sending email...")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
print("Email sent!")