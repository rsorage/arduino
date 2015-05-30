__author__ = 'root'

import smtplib
import ConfigParser

config = ConfigParser.ConfigParser()
config.readfp(open('smart_alarm.conf'))

user = 'alarm@system.com'
passwd = '************'

receivers = 'john.doe@gmail.com'
message = """From: Casa Inteligente <alarm@system.com>
To: John Doe <john.doe@gmail.com>
MIME-Version: 1.0
Content-type: text/html
Subject: Movimento detectado em sua casa

<h1>Um movimento foi detectado em sua casa!</h1>
<h3>Responda esse email com "desativar" para desarmar o alarme...</h3>
"""


def send():
    smtp_srv = config.get('mail', 'smtp.server')
    smtp_port = config.getint('mail', 'smtp.port')
    smtp_ssl = config.getboolean('mail', 'smtp.ssl')

    if smtp_ssl:
        smtp_server = smtplib.SMTP_SSL(smtp_srv, smtp_port)
    else:
        smtp_server = smtplib.SMTP(smtp_srv, smtp_port)
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.login(user, passwd)
    smtp_server.sendmail(user, receivers, message)
    smtp_server.close()
    print('Email successfully sent!')
