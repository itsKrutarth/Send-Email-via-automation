import smtplib
import datetime as dt
import random

quote = ""
now = dt.datetime.now()
if(now.weekday()==0):
    with open("quotes.txt", "r") as quotesFile:
        content = quotesFile.readlines()
        quote = content[random.randint(0, len(content))]
        
    myEmail = "YOUR_EMAIL@gmail.com"
    myPassword = "APP_PASSWORD"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(myEmail, myPassword)
        connection.sendmail(from_addr=myEmail, to_addrs="RECIEVER_EMAIL@gmail.com", msg=f"Subject: Quote of the Week! \n\n{quote}")

print("Email sent!")