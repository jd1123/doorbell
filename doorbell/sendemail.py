import smtplib
from doorbell import app

#this can be used to send gmail

def send_email(msg = ''):
    # SMTP_SSL Example
    try:
        server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server_ssl.ehlo() # optional, called by login()
        server_ssl.login(app.config['gmailLogin'], app.config['gmailPassword'])  
        # ssl server doesn't support or need tls, so don't call server_ssl.starttls()
        TO = app.config["toNumbers"]
        FROM = app.config["gmailLogin"]
        SUBJECT = "Someone is at the door"
        TEXT = "Someone is at the door" + " " + msg
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        server_ssl.sendmail(FROM, TO, message)
       # server_ssl.quit()
        server_ssl.close()
        print 'successfully sent the mail'
    except:
        print 'failed'

def send_email_TLS():
    import smtplib
    recipient = app.config['toNumber']
    gmail_user = app.config['gmailLogin']
    gmail_pwd = app.config['gmailPassword']
    FROM = gmail_user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = "Someone is at the door"
    TEXT = "Someone is at the door"

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"
