import smtplib, os.path
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders

GMAIL_USER = "dev@acvaa.org"
GMAIL_PWD = "d4E.z6XhwfD+dbNosqGF"
MAIL_SERV = "smtp.gmail.com"
MAIL_PORT = 587

def create_msg (to_addr, subject, text, files=[]):
    msg = MIMEMultipart()
    msg['From'] = GMAIL_USER
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.attach(MIMEText(text))
    for file in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(file,"rb").read() )
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
        msg.attach(part)
    return msg

def send_email (to_addr, msg):
    mailServer = smtplib.SMTP(MAIL_SERV, MAIL_PORT)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(GMAIL_USER, GMAIL_PWD)
    mailServer.sendmail(GMAIL_USER, to_addr, msg.as_string())
    mailServer.close()

def send_registration_confirm(to_addr, userid):
    a = []
    a.append('Congratulations! Your registration with the ACVAA website was successful.')
    a.append('')
    a.append('Your user name for the site is: %s' % (userid))
    a.append('')
    a.append('Don\'t lose it! You\'ll need it to log into the site now & in the future.')
    a.append('')
    a.append('Thanks for taking the time to register & we look forward to serving you well with our new website.')
    a.append('')
    text = '\r\n'.join(a)
    msg = create_msg(to_addr, 'ACVAA Welcome Message', text)
    send_email(to_addr, msg)

def send_reset_password(to_addr, newpass):
    a = []
    a.append('Your password for the ACVAA website has been reset.')
    a.append('')
    a.append('Your new password is: %s' % (newpass))
    a.append('')
    a.append('To successfully log in, you will also need your site username. For security purposes, it is not included in this email.')
    a.append('')
    a.append('After logging in, please access your account and change your password to something that will be easy for you to remember.')
    a.append('')
    a.append('If you did not request this change or cannot remember your ACVAA site username, please contact an ACVAA site administrator at once.')
    a.append('')
    a.append('Thank you.')
    a.append('')
    text = '\r\n'.join(a)
    msg = create_msg(to_addr, 'ACVAA Password Reset', text)
    send_email(to_addr, msg)

