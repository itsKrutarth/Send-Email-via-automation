import smtplib

myEmail = "xyz@gmail.com"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()

