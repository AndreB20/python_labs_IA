from hashlib import new

import requests
from bs4 import BeautifulSoup
import smtplib

sender = 'nu_vreau_spam@coneasorin.ro'
subject = 'Pretul a scazut la'
to_addr_list = ['andreiburlacu2000@gmail.com']
cc_addr_list = ['']
def sendemail(sender,message,subject,to_addr_list,cc_addr_list=[]):
    try:
        smtpserver='mail.x-it.ro:26'
        header = 'From: %s\n' % sender
        header += 'To: %\n' % ','.join(to_addr_list)
        header += 'Cc: %\n' % ','.join(cc_addr_list)
        header += 'Subject: %s\n\n' % subject
        message = header + message

        server = smtplib.SMTP(smtpserver)
        server.starttls()
        server.login(sender, "stiinte216_2022")
        problems = server.sendemail(sender, to_addr_list, message)
        server.quit()
        return True
    except:
        print("Error: unable to send email !")
        return False

def data_scrapping():
    req = requests.get("https://www.emag.ro/telefon-mobil-apple-iphone-14-pro-max-256gb-5g-deep-purple-mq9x3rx-a/pd/DJDY4LMBM/")
    soup = BeautifulSoup(req.text, 'html.parser')
    price = soup.find('p', attrs = {'class':'product-new-price'}).text
    price = price.replace(".","")
    price = price.replace(",",".")
    price = price.replace(" Lei", "")
    new_price= float(price)
    if(new_price<7999):
        sendemail(sender,"Speram sa nu fie teapa",subject,to_addr_list,cc_addr_list=[])
        print("Avem modificare de pret !")
    else:
        print("n avem nica")
    print(new_price)

data_scrapping()