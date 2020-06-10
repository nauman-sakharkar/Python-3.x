print("-------------------------------------------\nNauman - 648\n-------------------------------------------")
import urllib.request
r=urllib.request.urlopen('https://www.google.co.in/')
print(r.read())

print("-------------------------------------------\nNauman - 648\n-------------------------------------------")
import smtplib
password='naumannauman'
sender ='naumansakharkar@gmail.com'
receivers = 'naumansakharkar@gmail.com'
content='''From : <naumansakharkar@gmail.com>
To : <naumansakharkar@gmail.com>
Subject : Nauman
asdhai ofdsjoids'''
mail= smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()   
mail.starttls()
try:
    mail.login('naumansakharkar@gmail.com',password)
    mail.sendmail('naumansakharkar@gmail.com','naumansakharkar@gmail.com',content)
    mail.close()
    print ("Successfully sent email")
except:
    print ("Unsuccessful")
