import datetime as dt
import os
import random
import smtplib

MY_EMAIL = "testesmtp100dias@gmail.com"
PASSWORD = "qycqmoqgkvhutelj"
PORT = 587

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    # Constrói o caminho absoluto para o arquivo quotes.txt
    # Isso garante que o script funcione mesmo quando executado pelo cron
    script_dir = os.path.dirname(os.path.abspath(__file__))
    quotes_path = os.path.join(script_dir, "quotes.txt")
    # É uma boa prática especificar o encoding, especialmente com textos em português.
    with open(quotes_path, encoding="utf-8") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com", port=PORT) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        # A mensagem precisa ser codificada em UTF-8 para suportar caracteres especiais.
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="braulio.truylio@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{quote}".encode("utf-8")
        )
