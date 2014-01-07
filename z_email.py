import smtplib, time

#FRADDR = 'gary@eringary.com'
FRADDR = 'dev@acva.org'
MAILSERV = 'localhost'

def get_timestamp():
    return time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(time.time()))

def send_email(from_addr, subject, to_addr, msg):
    a = 'Date: %s\r\n' % (get_timestamp())
    a += 'From: %s\r\n' % (from_addr)
    a += 'Subject: %s\r\n' % (subject)
    a += 'To: %s\r\n' % (to_addr)
    a += '\r\n'
    a += msg
    server = smtplib.SMTP(MAILSERV)
    server.set_debuglevel(0)
    server.sendmail(from_addr, to_addr, a)
    server.quit()

def send_registration_confirm(to_addr, userid):
    a = []
    a.append('Congratulations! Your registration with the ACVA website was successful.')
    a.append('')
    a.append('Your user name for the site is: %s' % (userid))
    a.append('')
    a.append('Don\'t lose it! You\'ll need it to log into the site now & in the future.')
    a.append('')
    a.append('Thanks for taking the time to register & we look forward to serving you well with our new website.')
    a.append('')
    msg = '\r\n'.join(a)
    send_email(FRADDR, 'ACVA Welcome Message', to_addr, msg)

def send_reset_password(to_addr, newpass):
    a = []
    a.append('Your password for the ACVA website has been reset.')
    a.append('')
    a.append('Your new password is: %s' % (newpass))
    a.append('')
    a.append('To successfully log in, you will also need your site username. For security purposes, it is not included in this email.')
    a.append('')
    a.append('After logging in, please access your account and change your password to something that will be easy for you to remember.')
    a.append('')
    a.append('If you did not request this change or cannot remember your ACVA site username, please contact an ACVA site administrator at once.')
    a.append('')
    a.append('Thank you.')
    a.append('')
    msg = '\r\n'.join(a)
    send_email(FRADDR, 'ACVA Password Reset', to_addr, msg)

