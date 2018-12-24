import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

'''Send emails keeping cc'''

dest = "sjistheboss@gmail.com"
cc = "hasibzunair@gmail.com"

subject = "Its me"
message = "Hi there!"

src = "techacademy1234@gmail.com"
password = "t3chn0tt@b0t5"

msg = MIMEMultipart()
msg['From'] = src
msg['Subject'] = subject
msg['To'] = dest
msg["cc"] = cc 
msg.attach(MIMEText(message, 'plain'))

def send_email(src, dest, cc):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(src, password)
    text = msg.as_string()
    server.sendmail(src, [dest,cc], text)
    server.quit()
    print("Sent!")


send_email(src, dest, cc)
