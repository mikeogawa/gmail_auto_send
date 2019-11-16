#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 10:16:31 2018

@author: mikeogawa
!!!!note!!!!
activate lower level secuirty access at :https://myaccount.google.com/lesssecureapps
before sending!!!!
"""

import smtplib
import os
import re
from email.mime.text import MIMEText
from email.utils import formatdate

list_of_dir=[f for f in os.listdir("mail_list") if not f.startswith('.')]
print(list_of_dir)

FROM_ADDRESS = ''
LOG_IN = ''
MY_PASSWORD = ''

CC =''
SUBJECT = ''


def create_message(from_addr, to_addr, bcc_addrs, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Cc'] = bcc_addrs
    msg['Date'] = formatdate()
    return msg


def send(from_addr, to_addrs, msg):
    #    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj = smtplib.SMTP_SSL("smtp.gmail.com", 465) 
    smtpobj.ehlo()
    smtpobj.login(LOG_IN, MY_PASSWORD)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()

for title in list_of_dir:
    with open("mail_list/"+title) as f:
        text=f.readlines()
        TO_ADDRESS=re.sub('\n','',text[0])
        BODY=text[2:]
        BODY2="".join(BODY)        
        msg = create_message(FROM_ADDRESS, TO_ADDRESS, CC, SUBJECT, BODY2)
        send(FROM_ADDRESS, [TO_ADDRESS, CC],msg)
    

