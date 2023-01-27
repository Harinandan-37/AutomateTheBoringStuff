import requests, bs4
import time, os

comic = 1
comic_number = 2729 #default comic number to download if no comic exists.
comicFiles = os.listdir('/home/shrisharanyan/comics')

#checks my last comic downloaded 
for i in range(len(comicFiles)):
    comicFiles[i] = int(comicFiles[i])

comicFiles.sort()

if len(comicFiles) != 0:
    comic_number = comicFiles[-1]

os.chdir('/home/shrisharanyan/comics')
path = os.getcwd()

#I found its easier to define a function to download and its neater as well.
def downloadComic():
    global comic
    global comic_number
    url = 'https://xkcd.com/' + str(comic_number) + '/'
    try:
        
        print()
        print("Downloading page %s  ..." % url)
        res = requests.get(url)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        comicElem = soup.select('#comic img')
        if comicElem == []:
            print("Could not find comic image..")
        else:
            #this is the actual link for the image. 
            comicUrl = 'https:' + comicElem[0].get('src')
            res = requests.get(comicUrl)
            res.raise_for_status()
            print()
            print('Downloading image %s   ...' % (comicUrl))

            imageFile = open(os.path.join(path,str(comic_number)),'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
            comic += 1
            comic_number += 1

        url = 'https://xkcd.com/' + str(comic_number) + '/'
        print()
        print("-----------------------------------")
        print("Checking: " + url)
        print()


    except requests.exceptions.HTTPError:
        print()
        print('No comic was found. Will try again in a few hours')
        print()
        print("-----------------------------------")
    
    time.sleep(5) # acc to the question it should be (24 * 3600) secs. But its easier to check if it works if its 5 secs.

for i in range(5): #acc to the question checking once a day is enough, but for checking I've set it as 5 times.
    print()
    print('Searching for a new comic...')
    downloadComic()


