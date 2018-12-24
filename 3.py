import smtplib

'''Send email to multiple persons'''

subject = "I am a computer program"
msg = "Hello there!"
dests = ["hasibzunair@gmail.com", "sjistheboss@gmail.com"]

src = "techacademy1234@gmail.com"
password = "t3chn0tt@b0t5"

def send_email(subject, msg, email):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(src, password)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(src, email, message)
        server.quit()
    except:
        print("Email failed to send.")


subject = "I am a computer program"
msg = "Hello there!"

for email in dests:
    send_email(subject, msg, email)
