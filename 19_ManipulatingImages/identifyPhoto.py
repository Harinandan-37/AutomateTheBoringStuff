import os
from PIL import Image as img

for folderName, subFolders, filenames in os.walk('/home/shrisharanyan/'):
    try:
        numPhotoFiles = 0
        numNonPhotoFiles = 0

        for filename in filenames:
            filename = os.path.join(folderName,filename)
            if not(filename.endswith('.jpg') or filename.endswith('.png')):
                numNonPhotoFiles += 1
                continue
            else:
                im = img.open(filename)
                width, height = im.size
                if not(width >  500 and height >  500):
                    numNonPhotoFiles += 1
                    continue
                else:
                    numPhotoFiles += 1
            
        if numPhotoFiles > (numPhotoFiles+numNonPhotoFiles)/2:
            print(f"'{folderName}' is a photo folder!!")
    except:
        continue