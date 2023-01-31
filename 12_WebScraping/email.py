#usage: python3 email.py start
from selenium import webdriver
from selenium.webdriver.common.keys import Keys




print("\nWelcome to email_bot!! This is an automated email sender! We'll save you the trouble of going to the website and using the GUI for small emails.\n")
print('Please fill in the necessary details...\n')
email_id = input("Enter your username: \n")
email_pwd = input("Enter your password: \n")
email_recipient = input("Recipient email address: \n")
email_subject = input("Email subject: \n")
email_body = input("Email body: \n")

print()

browser = webdriver.Firefox()
browser.get('http://mail.google.com')

login_email = browser.find_element_by_id('identifierId')
login_email.send_keys(email_id)
id_next = browser.find_element_by_id('identifierNext')
id_next.click()

login_pwd = browser.find_element_by_name('Passwd')
login_pwd.send_keys(email_pwd)
pwd_next = browser.find_element_by_id('passwordNext')
pwd_next.click()

email = browser.find_element_by_tag_name('html')
compose = browser.find_element_by_class_name('T-I T-I-KE L3')
compose.click()
email.send_keys(Keys.TAB)
email.send_keys(email_recipient)
email.send_keys(Keys.TAB)
email.send_keys(email_subject)
email.send_keys(Keys.TAB)
email.send_keys(email_body)
email.send_keys(Keys.ENTER)

print("\nEmail Sent\n")




