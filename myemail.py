from flask_mail import Message
from flask import render_template
from app import mail

subject_pref = 'blog'
sender_email ='kipfrankline@gmail.com'

def mail_message(subject,template,to,**kwargs):

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)

