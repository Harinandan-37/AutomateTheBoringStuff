#usage: python3 email.py start
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

# THERE IS A PROBLEM WITH RUNNING PROGRAMS FROM MY DASH
# HOWEVER TO USE COMMAND LINE, WE CAN MAKE A .sh FILE, DESKTOP FILE AND MAKE PROGRAM FILE YOU CAN RUN FROM DASH.
# THIS OPENS A GNOME TERMINAL. 
# BUT MINE SAYS THAT MY CODE DOESN'T EXIST IN THE DIRECTORY WHEN IT VERY CLEARLY DOES.


print("\nWelcome to email_bot!! This is an automated email sender! We'll save you the trouble of going to the website and using the GUI for small emails.\n")
print('Please fill in the necessary details...\n')
email_id = input("Enter your username: \n")

email_pwd = input("\nEnter your password: \n")
email_recipient = input("\nRecipient email address: \n")
email_subject = input("\nEmail subject: \n")
email_body = input("\nEmail body: \n")

print()

browser = webdriver.Chrome()

browser.get('http://mail.google.com')

# CHROME PREVENTS BOT FROM SIGNING IN.
# BUT I FOUNT OUT THAT YOU CAN CREATE AN ACCOUNT IN THE AUTOMATED WINDOW.
# AND THEN EXIT THE PROGRAM AND RUN IT AGAIN. THE NEWLY CREATED ACCOUNT STILL WORKS.
# THE ACCOUNT CAN BE USED EVERYTIME FOR SELENIUM.


login_email = browser.find_element_by_id('identifierId')
login_email.send_keys(email_id)
id_next = browser.find_element_by_id('identifierNext')
id_next.click()

time.sleep(5)

login_pwd = browser.find_element_by_name('Passwd')
login_pwd.send_keys(email_pwd)
pwd_next = browser.find_element_by_id('passwordNext')
pwd_next.click()

time.sleep(5)
email = browser.find_element_by_tag_name('html')
compose = browser.find_element_by_class_name('z0')

compose.click()

time.sleep(2)
print("Writing....")


rec = browser.find_elements_by_id(':c1')

rec[0].send_keys(email_recipient)
print("Entered recipient id...")

rec[0].send_keys(Keys.ENTER)
sub = browser.find_elements_by_id(':83')
sub[0].click()
sub[0].send_keys(email_subject)
print("Entered Subject...")
time.sleep(1)

body = browser.find_elements_by_id(':9c')
body[0].click()
body[0].send_keys(email_body)
print("Entered Body...")

time.sleep(2)

send = browser.find_elements_by_id(':7t')
send[0].click()


print("\nEmail Sent\n")
time.sleep(1000)



