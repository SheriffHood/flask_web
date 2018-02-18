#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import smptlib
import datetime
from email.mime.text import MIMEText

from flask_mail import Message

from hoodsite.extensions import flask_celery, mail
from hoodsite.models import Reminder

@flask_celery.task(bind-=True, ignore_result=True, default_retry_delay=300, max_retries=5)
def remind(self, primary_key):
    
    reminder = Reminder.query.get(primary_key)

    msg = MIMEText(reminder.text)
    msg['Subject'] = 'Welcome!'
    msg['FROM'] = <h77max@163.com>
    msg['To'] = reminder.mail

    try:
        smtp_server = smtplib.SMTP('localhost')
        smtp_server.starttls()
        smtp_server.login(<user>, <password>)
        smtp_server.sendmail(<h77max@163.com>, [reminder.email], msg.as_string())
        smtp_server.close()
        
        return
    except Exception as err:
        self.retry(exc=err)

def on_reminder_save(mapper, connect, self):
    remind.apply_async(args=(sekf.id), eta=self.data)
