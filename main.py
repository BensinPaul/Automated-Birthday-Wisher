import pandas
import smtplib
import datetime as dt
import random
email = "bensin0paul@gmail.com"
password = 'etol uspf rfmr vxpf'

now = dt.datetime.now()
today = (now.month, now.day)
birthdays = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]):data_row for (index,data_row) in birthdays.iterrows()}
if today in birthday_dict:
    random_letter = random.randint(1,3)
    with open(f"letter_templates/letter_{random_letter}.txt") as file:
        text = file.read()
        letter = text.replace("[NAME]", birthday_dict[today]["name"])

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user = email, password = password)
    connection.sendmail(
        from_addr = email,
        to_addrs = birthday_dict[today]["email"],
        msg = f"Subject:Happy Birthday {birthday_dict[today]["name"]}\n\n{letter}"
    )


