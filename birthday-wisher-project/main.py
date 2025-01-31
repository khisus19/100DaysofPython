import random, datetime, smtplib
import pandas as pd

my_gmail = "pruebapython5@gmail.com"
gmail_server = "smtp.gmail.com"
gmail_app_pwd = "llea bnmy oldl ysgl"
yahoo_server = "smpt.mail.yahoo.com"

## Extract todays date
today = datetime.datetime.now()
month_today = today.month
day_today = today.day

## Read the csv file and convert it to a dictionary to work with
df = pd.read_csv("./birthdays.csv")
birthdays_dict = df.to_dict("records")


## Loop through all the birthdays to check if today is someones birthday
for date in birthdays_dict:
    if date["month"] == month_today and date["day"] == day_today:

## If is true we pick a random letter and replace the birthday person's name
        with open(f"./letter_templates/letter_{random.randint(1,3)}.txt", "r") as letter_file:
            letter_content = letter_file.read()
            letter_content = letter_content.replace("[NAME]", date["name"])

## Send the letter generated in step 3 to that person's email address.

        with smtplib.SMTP(gmail_server, port=587) as connection:
            connection.starttls()
            connection.login(user=my_gmail, password=gmail_app_pwd)
            connection.sendmail(
                from_addr=my_gmail,
                to_addrs=date["email"],
                msg=f"Subject:Happy Birthday!!\n\n{letter_content}"
            )



