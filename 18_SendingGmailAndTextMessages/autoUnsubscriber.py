import bs4, imapclient

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('boomchingshaka@gmail.com','Boomchingshaka1')

