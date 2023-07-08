#!/usr/bin/env python3

import sys, smtplib, socket

from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText

try:
    msg = MIMEText("Message 1 Say HI", 'plain')
    msg['Subject'] = "Message for Martin Y"
    msg['From'] = 'pyyanev@gmail.com'

    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.set_debuglevel(True)
    smtp.ehlo()

#TSL is a encryption protocol
    if smtp.has_extn('STARTTLS'):
        smtp.starttls()
        smtp.ehlo()

#Adding creditals
    try:
        smtp.login("pyyanev@gmail.com", "")
    except smtplib.SMTPException as e:
        print("Authentication error", e)
        sys.exit(1)
#Sending the email
    try:
        smtp.sendmail('pyyanev@gmail.com', ['mpyanev@gmail.com'], msg.as_string())
    except(socket.gaierror, socket.error, socket.herror, smtplib.SMTPException) as e:
        print(" Your message has not been sent")
        print(e)
        sys.exit(1)
    finally:
        smtp.quit()

except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException) as e:
    print("Message has not been sent!!!")
    print(e)
    sys.exit(1)


















