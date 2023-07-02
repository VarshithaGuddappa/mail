from smtplib import SMTP_SSL# to create smtp connection and ssl to secure and encrypt data so no one can see
from email.message import EmailMessage#used to structure mail like header,content etc
import os
import json#using login credentials from cred.login file

file=open("cred.json")
 
data=json.load(file)
print(data)


SENDER_EMAIL=data["email"]
MAIL_PASSWORD=data["password"]

def send_mail(SENDER_EMAIL,RECEIVER_EMAIL,MAIL_PASSWORD,subject,content):
    msg=EmailMessage()
    msg["From"]=SENDER_EMAIL
    msg["To"]=RECEIVER_EMAIL
    #msg["Cc"]=CC_EMAIL
    #msg["Bcc"]=BCC_EMAIL
    msg["Subject"]=subject
    msg.set_content(content)

    print(msg)
    
    # creating connection
    #sending mail via smtp server
    with SMTP_SSL("smtp.gmail.com",465) as smtp:
        smtp.login(SENDER_EMAIL,MAIL_PASSWORD)
        smtp.send_message(msg)
        smtp.close()#recommended to close
    print("mail sent successfully")

RECEIVER_EMAIL="harshith.7909@gmail.com"
subject="Test subject"
content="""
hey you
this is a test mail

Thank you
Regards
Varsh
"""
send_mail(SENDER_EMAIL,RECEIVER_EMAIL,MAIL_PASSWORD,subject,content)
