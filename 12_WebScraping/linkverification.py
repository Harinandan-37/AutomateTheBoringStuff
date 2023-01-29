import requests, bs4
import os

url = 'https://www.google.com'
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

links = soup.select('a')

cwd = os.getcwd()
os.makedirs('links', exist_ok=True)

path = os.path.join(cwd,'links')

i = 1

for link in links:
    linkfile = str(i) + '.txt'
    pathc = os.path.join(path,linkfile)
    link = link.get('href')
    file1 = open(pathc,'wb')
    try:
        response = requests.get(link)
        if res.status_code == 404:
            print ('404 ERROR: ' + link + ' not found')
        else:
            print( 'Working Link: ' + link)
            for chunk in response.iter_content(100000):
                file1.write(chunk)
            i+=1
            continue
    except:
        continue
    
