import pandas
import datetime as dt
import random
import smtplib

my_email = "arrow9129402fahad@gmail.com"
password = "ookcpkhuiwglgxup"
now = dt.datetime.now()
today_month = now.month
today_day = now.day
letter_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
birth_details = pandas.read_csv("birthdays.csv")
birth_dict = birth_details.to_dict(orient="records")
for i in birth_dict:
    birth_month = i['month']
    birth_date = i['day']
    if today_month == birth_month and today_day == birth_date:
        the_letter = random.choice(letter_list)
        with open(the_letter) as letter:
            content = letter.read()
            x = content.replace("[NAME]", i['name'])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=f"{i['email']}",
                                msg=f"Subject:Happy Birthday!\n\n{x}")
