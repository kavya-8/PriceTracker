# main/price_tracker.py
import requests
from bs4 import BeautifulSoup
import datetime
import smtplib
import csv

def track_price(url, desired_price, user_email):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "X-Amzn-Trace-Id": "Root=1-666ee1ca-3b7cb3a437c1f00a1530006d"
    }
    page = requests.get(url, headers=header)
    soup = BeautifulSoup(page.content, "html.parser")
    soup1 = BeautifulSoup(soup.prettify(), "html.parser")
    
    title = soup1.find(id='productTitle').get_text().strip()
    price = soup1.find(class_='a-price-whole').get_text().strip()
    price = price.replace(',', '')
    price = price[:5]
    price = int(price)

    today = datetime.date.today()
    data = [title, price, today]

    with open('AmazonDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(['Product Name', 'Price', 'Date'])
        writer.writerow(data)

    if price < desired_price:
        send_mail(user_email, title, price)

def send_mail(recipient_email, product_name, current_price):
    try:
        smtp_server = 'smtp.gmail.com'
        port = 465
        sender_email = 'mythresh7@gmail.com'
        password = 'mkbbflxlqjzofpxj'
        
        server = smtplib.SMTP_SSL(smtp_server, port)
        server.login(sender_email, password)
        
        subject = f"Price Drop Alert: {product_name}"
        body = f"The price of {product_name} has dropped to {current_price}. Now is your chance to buy!"
        message = f'Subject: {subject}\n\n{body}'
        
        server.sendmail(sender_email, recipient_email, message)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
    finally:
        server.quit()
