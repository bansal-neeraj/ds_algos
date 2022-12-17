import imaplib
import email
from datetime import date
from html.parser import HTMLParser

class HTMLFilter(HTMLParser):
    text = ""
    def handle_data(self, data):
        self.text += data + '\n'
        # print('handle_data called')

imap_server = "imap.gmail.com"
email_address = "neerajbansal152@gmail.com"
password = "@puneet123"

imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_address,password)
imap.select("Inbox")

srh_date = date(2022,2,1).strftime("%d-%b-%Y")
_, msgnums = imap.search(None,f'(SINCE {srh_date})')
# _, msgnums = imap.search(None,'(SINCE "01-FEB-2022")')
# _, msgnums = imap.search(None,"ALL")
my_messages = []
for msgnum in msgnums[0].split():
    email_data = {}
    _, data = imap.fetch(msgnum,"(RFC822)")
    # print(email.message_from_string(data[0][1]))


    _,mg = data[0]
    e_message = email.message_from_bytes(mg)
    # print(e_message)

    print(f"Message from: {email.message_from_bytes(msgnum)}")
    # print(f"Message from: {message.get('From')}")
    #
    print ('*'*15)
    for header in ['subject','to','from','date']:
        print("{}: {}".format(header,e_message[header]))
        email_data[header] = e_message[header]

    for part in e_message.walk():
        if part.get_content_type() == "text/plain":
            # print(part.as_string())
            body = part.get_payload(decode=True)
            # print(body)
            # print(body.decode())
            email_data['body'] = body.decode()

        elif part.get_content_type() == "text/html":
            html_body = part.get_payload(decode=True)
            # print(html_body)
            # print(html_body.decode())
            f = HTMLFilter()
            f.feed(html_body.decode())
            print(f.text)

            email_data['body'] = html_body.decode()
    my_messages.append(email_data)

# print(my_messages)

imap.close()



