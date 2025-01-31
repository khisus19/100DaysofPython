import random, datetime, smtplib
import pandas as pd

my_gmail = "pruebapython5@gmail.com"
gmail_server = "smtp.gmail.com"
gmail_app_pwd = "llea bnmy oldl ysgl"
my_yahoo = "pythonrecipient@yahoo.com"
yahoo_server = "smpt.mail.yahoo.com"


##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

today = datetime.datetime.now()
year_today = today.year
month_today = today.month
day_today = today.day

df = pd.read_csv("./birthdays.csv")
birthdays_dict = df.to_dict("records")

for date in birthdays_dict:
    if date["month"] == month_today and date["day"] == day_today:
        print(f"El cumpleaño de {date["name"]} es este mes. Cumple el {date["day"]}")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv


# 4. Send the letter generated in step 3 to that person's email address.




