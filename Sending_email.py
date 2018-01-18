import smtplib           # inbuilt in python version 3.5 and higher
import time

def send_mail(sender, recipient, password, subject, text):
    smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp_server.login(sender, password)
    message = "Subject: {}\n\n{}".format(subject, text)
    smtp_server.sendmail(sender, recipient, message)
    smtp_server.close()

def mail():
    sender = "sender@gmail.com"
    recipient = "reciever@yahoo.in"
    password = "YourPassword" # Your SMTP password for Gmail
    subject = "Good Morning"
    text = get_text()
    send_mail(sender, recipient, password, subject, text)
    
def get_text():
    day = time.strftime('%d of %m %Y')
    return "Good Morning! Today is the"+day+"Have an awesome Blossom Day"

if __name__ == "__main__":
    mail()    