#1. Create an SFTP object to connect to the server
#2. Log In to account
#3. Define headers for the message and login creditals
#4. Crreate a MIMEMultipart message object
#5. Attach the message to the MIMEMultipart object
#6. Send the message

from email.mime.multipart import MIMEMultipart
from email.mime.text import  MIMEText
import smtplib

message = MIMEMultipart()

import getpass

username = input('Username: ')
password = getpass.getpass(prompt="Password: ")

message['From'] = username
message['To'] = username
message['Subject'] = " Sending Email to Myself"

message.attach(MIMEText("Hello this is an email from yourself to yourself. It is fun isnt it", 'plain'))

server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()

server.login(message['From'], password)

server.sendmail(message['From'], message['To'], message.as_string())
print("successfully sent to email: %s " % (message['To']))
server.quit()











