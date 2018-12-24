import json
import smtplib

'''Send a simple email and add a subject'''

subject = "I am a computer program"
msg = "Hello there!"
dest = "hasibzunair@gmail.com"

src = "techacademy1234@gmail.com"
password = "t3chn0tt@b0t5"

def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(src, password)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(src, dest, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


send_email(subject, msg)