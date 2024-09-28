import smtplib
import getpass


s = smtplib.SMTP("smtp-mail.outlook.com",587)
s.starttls()
s.ehlo
try:
    s.login("recall.testing1@outlook.com", "testing$12")
except SMTPAuthenticationError:
    print ('SMTPAuthenticationError')
s.sendmail("recall.testing1@outlook.com", "kritika.singh14@outlook.com", "hi")
print("hi")
s.quit()