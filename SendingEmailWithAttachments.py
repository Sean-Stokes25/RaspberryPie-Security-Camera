#------------------------------
#Email sending with attachments
#------------------------------
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(sender, password, reciever, subject ,body, filename):
    #creates email
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = reciever
    message["Subject"] = subject

    message.attach(MIMEText(body,"plain"))
    #ataches the file
    with open (filename,"rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment; filename="+filename)
    message.attach(part)

    #connects to gmail server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    #signs into senders account and sends email to reciever
    try:
        server.login(sender , password)
        print("logged in")
        server.sendmail(sender,reciever,message.as_string())
        print("Email has been sent")

    except smtplib.SMTPAuthenticationError:
        print("unable to sign in")



