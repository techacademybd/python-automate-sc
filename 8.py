import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

'''Send emails to group reciepients from a text file

    - Add list of emails in the text file
    - Script send email to all of them in a group, not individually
'''

text_file = open("8.txt", "r")
dest = ""
for line in text_file:
    dest += line[:-1] + ","

dests = dest[:-1]

subject = "Its me"
message = "Hi there!"

src = "techacademy1234@gmail.com"
password = "t3chn0tt@b0t5"

msg = MIMEMultipart()
msg['From'] = src
msg['To'] = dests
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

def send_email(src, dests):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(src, password)
    text = msg.as_string()
    server.sendmail(src, dests, text)
    server.quit()
    print("Sent!")

send_email(src, dests.split(','))