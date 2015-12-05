#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import thread
import settings


def send_mail(sender, reciever, subject, body, server):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = reciever
    html = body
    msg.attach(MIMEText(html, 'html', _charset='utf8'))
    s = smtplib.SMTP(server)
    try:
        s.sendmail(sender, reciever, msg.as_string())
        return True
    except Exception, e:
        return False
    finally:
        s.quit()

def send_notification(email, body, subject):
    return send_mail(settings.mail_from, email, subject, body, settings.mail_server)


def send_notification_async(email, body, subject):
    thread.start_new_thread(send_notification, (email, body, subject))

subjects = {
    1:{
        'en':'1st notif',
        'ro':'1st notif',
        'ru':'1st notif'
    },
    2:{
        'en':'1st notif',
        'ro':'1st notif',
        'ru':'1st notif'
    },
    3:{
        'en':'1st notif',
        'ro':'1st notif',
        'ru':'1st notif'
    }
}



