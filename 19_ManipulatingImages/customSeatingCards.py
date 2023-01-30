import os
from PIL import ImageFont, Image, ImageDraw

os.makedirs('invitations',exist_ok=True)

guestFile = open('guests.txt','rb')
guestList = guestFile.readlines()

for guest in guestList:

    cardIm = Image.new('RGBA', (288, 360), 'lightgrey')    

    # using catlogo instead of flower for now.
    flowerIm = Image.open('flower.png')
    flowerIm = flowerIm.resize((70, 70))
    draw = ImageDraw.Draw(cardIm)
    paraFont = '/usr/share/fonts/truetype/Gargi'
    paraText = ImageFont.truetype(os.path.join(paraFont,'Gargi.ttf'),12)

    draw.text((22,60),'It would be a pleasure to have the company of', fill='brown', font=paraText)

    nameFont = '/usr/share/fonts/truetype/abyssinica'
    nameText = ImageFont.truetype(os.path.join(paraFont,'AbyssinicaSIL-Regular.ttf'),17)
    guest = str(guest).strip('b\'').strip('\\r').strip('\\n').strip('\\r')
    draw.text((95,110), guest, fill='brown' ,font=nameText)

    draw.text((45,150),'at 11010 Memory Lane on the Evening of', fill='brown', font=paraText)
    draw.text((120,200),'April 1st', fill='brown', font=paraText,)
    draw.text((110,225),'at 7 o\'clock \n', fill='brown', font=paraText)
    draw.line([(10, 10), (277, 10), (277, 349), (10, 349), (10, 10)], fill='brown')
    draw.line([(0, 0), (287, 0), (287, 359), (0, 359), (0, 0)], fill='black')
    cardIm.paste(flowerIm,(0,0),flowerIm)
    cardIm.save(os.path.join('invitations',f'invite_to_{guest}.png'))

