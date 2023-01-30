import os
from PIL import Image as img
os.chdir('/home/shrisharanyan/')
SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = img.open(LOGO_FILENAME)
logoIm = logoIm.resize((75,75))
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)

for filename in os.listdir('.'):
    if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpeg') or filename.lower().endswith('.jpg') or filename.lower().endswidth('.bmp') or filename.lower().endswith('gif')) or filename == LOGO_FILENAME:
        continue
    im = img.open(filename)
    width, height = im.size

    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE/width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE/height) * width)
            height = SQUARE_FIT_SIZE
        
        print('Resizing %s... ' % (filename))
    
        im = im.resize((width, height))
    
    print('Adding logo to %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    im.save(os.path.join('withLogo',filename))
