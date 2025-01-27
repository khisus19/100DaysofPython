import smtplib

my_email = "pruebapython5@gmail.com"
password = "llea bnmy oldl ysgl"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="pythonrecipient@yahoo.com", msg="Hello")
connection.close()