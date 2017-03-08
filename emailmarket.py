from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
import pymongo
msg = MIMEMultipart()
msg['subject'] = 'Email de Propaganda - MONGO'
conteudo = open("/opt/emails/email.txt").read()
image = open('/opt/emails/python-para-hackers.jpeg', 'rb')
msgImage = MIMEImage(image.read())
image.close()
msgImage.add_header('Content-ID', '<image1>')
msg.attach(msgImage)
msg.attach(MIMEText(conteudo , 'html'))

client = pymongo.MongoClient()
database = client.email
emails = database.email.find()


for email in emails:
    print(email['email'] + " " + email['nome'])
    if len(email) > 0:
        mailer = smtplib.SMTP('smtp.gmail.com', 587)
        mailer.ehlo()
        mailer.starttls()
        mailer.ehlo()
        mailer.login('livedeepwebbrasil@gmail.com', 'senha!@#_')
        mailer.sendmail('livedeepwebbrasil@gmail.com', email['email'], msg.as_string())
        mailer.close()