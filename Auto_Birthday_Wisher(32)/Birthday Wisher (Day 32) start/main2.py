import datetime as dt
import smtplib
import pandas
import random

MY_GMAIL = "[Your mail ID]"
MY_PASSWORD = "[Password of Mail ID]"

today = (dt.datetime.now().month, dt.datetime.now().day)
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_GMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_GMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{content}"
        )