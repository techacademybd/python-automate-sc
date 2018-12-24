import imaplib
import email
from collections import defaultdict

'''Read the last few emails and display the message content'''

src = "techacademy1234@gmail.com"
password = "t3chn0tt@b0t5"

count = 2
book = {}

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(src, password)
mail.list()
mail.select("inbox")

# convert raw message block to READABLE text
def get_first_text_block(email_message_instance):
    maintype = email_message_instance.get_content_maintype()
    if maintype == 'multipart':
        for part in email_message_instance.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif maintype == 'text':
        return email_message_instance.get_payload()

# read emails from inbox
def get_email(counter): # counter: read how many emails?

    result, data = mail.search(None, "ALL")
    # data is a list
    ids = data[0]
    # ids is a space separated string
    id_list = ids.split()
    # get the latest email in the inbox stack
    
    counter = -counter
    latest_email_id = id_list[counter]

    # get raw email
    _, data = mail.fetch(latest_email_id, "(RFC822)")
    raw_email = data[0][1]

    decoded_raw_email = raw_email.decode()
    email_message = email.message_from_string(decoded_raw_email)
    # convert raw email to text
    message = get_first_text_block(email_message)
    # print(str(email.utils.parseaddr(email_message['From'])[0]))
    name = str(email.utils.parseaddr(email_message['From'])[0])

    return name, message


for i in range(count):
    i+=1
    name, msg = get_email(i)
    book[name] = msg


for name, message in book.items():
    print(name, message)


print("Done!")
