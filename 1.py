import smtplib

'''Send a simple email'''

msg = "Hello there!"
dest = "sjistheboss@gmail.com"

src = "techacademy1234@gmail.com"
password = "t3chn0tt@b0t5"

def send_email(msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(src, password)
        
        message = '{}'.format(msg)

        server.sendmail(src, dest, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


send_email(msg)