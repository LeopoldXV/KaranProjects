# Import smtplib for the actual sending function
import datetime
import os
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

smtp_server = "smtp.gmail.com"
smtp_port = 587
gmail_user = "dxmzmx@gmail.com"
gmail_app_password = os.environ['MAIL_PASS']

def send_email(upcoming):
    # Open the plain text file whose name is in textfile for reading.

    time_of_show = upcoming[3].strftime("%H:%M %B %d, %Y")
    # me == the sender's email address
    # you == the recipient's email address
    delta = (upcoming[3] - datetime.datetime.now()).seconds
    hours, remainder = divmod(delta, 3600)
    minutes, seconds = divmod(remainder, 60)
    remainder_time = ('{:02} sati {:02} minuta i {:02} sekundi'.format(int(hours), int(minutes), int(seconds)))

    msg = EmailMessage()
    # mozda ime showa u arg?...
    msg.set_content(f'Slijedeci Gospodin Savrseni pocinje u {time_of_show}')
    msg['Subject'] = f'Slijedeća epizoda Gospodina savršenog počinje za samo {remainder_time}!'
    msg['From'] = 'd'
    msg['To'] = 'dnsmndc@gmail.com'

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection
    server.login(gmail_user, gmail_app_password)
    server.sendmail(gmail_user, msg['To'], msg.as_string())
    server.quit()
    print("Email sent successfully!")

