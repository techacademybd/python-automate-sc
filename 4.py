import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

'''Send an email with attachments '''

dest = "hasibzunair@gmail.com"

subject = "Attachment"
message = "Find attached file below"
filename = "piglet.gif"

src = "techacademy1234@gmail.com"
password = "t3chn0tt@b0t5"

msg = MIMEMultipart()
msg['From'] = src
msg['To'] = dest
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

def load_attachment(filename):
    attachment = open(filename, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    
    msg.attach(part)

def send_email(src, dest):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(src, password)
    text = msg.as_string()
    server.sendmail(src, dest, text)
    server.quit()
    print("Sent!")

load_attachment(filename)
send_email(src, dest)
