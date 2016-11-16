#Simplify labeling of HS data:

#M. Miller, 2016

import os
from PIL import Image

path = "/Users/matthewmiller/Dropbox/Research/Urban/Projects/HomeSearch/Images"

y = []
i = 0

for f in os.listdir(path):
    if ".jpg" in f:
        f = path + '/' + f
        img = Image.open(f)
        img.show()
        hl = raw_input('Does this image contain evidence of homelessness? (Y/N)')
        y = y + [hl]
        i += 1
    
    
    


