import smtplib

my_gmail = "pruebapython5@gmail.com"
gmail_server = "smtp.gmail.com"
gmail_app_pwd = "llea bnmy oldl ysgl"
my_yahoo = "pythonrecipient@yahoo.com"
yahoo_server = "smpt.mail.yahoo.com"

# connection = smtplib.SMTP("smtp.gmail.com", 587)
# connection.starttls()
# connection.login(user=my_yahoo, password=password)
# connection.sendmail(from_addr=my_yahoo, to_addrs=my_gmail, msg="Subject:Hello\n\nEmail with subject")
# connection.close()

# with smtplib.SMTP(gmail_server, port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_gmail, password=gmail_app_pwd)
#     connection.sendmail(
#         from_addr=my_gmail,
#         to_addrs=my_yahoo,
#         msg="Subject:28 de enero\n\nEmail with subject"
#     )

import random
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()



date_of_birth = dt.datetime(year=1987, month=7, day=17)


with open("./quotes.txt", "r") as quotes_file:
    quotes_list = quotes_file.readlines()
    todays_quote = random.choice(quotes_list).split(" - ")
    quote = todays_quote[0]
    quote_author = todays_quote[1]

with smtplib.SMTP(gmail_server, port=587) as connection:
    connection.starttls()
    connection.login(user=my_gmail, password=gmail_app_pwd)
    connection.sendmail(
        from_addr=my_gmail,
        to_addrs=my_gmail,
        msg=f"Subject:Today's quote is from {quote_author}\n\nQUOTE: {quote}\n{quote_author}"
    )

print(todays_quote)