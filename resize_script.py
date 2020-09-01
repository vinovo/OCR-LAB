from PIL import Image
import os, sys
import cv2 
import numpy as np 

if len(sys.argv) != 2:
    sys.exit('Require target folder path: [folder_path]')

TARGET_FOLDER = sys.argv[1]
dirs = os.listdir(TARGET_FOLDER)

def resize():
    for item in dirs:
        if os.path.isfile(TARGET_FOLDER+item) and item != '.DS_Store':
            im = Image.open(TARGET_FOLDER+item)
            f, e = os.path.splitext(TARGET_FOLDER+item)
            imResize = im.resize((400,400), Image.ANTIALIAS)
            imResize.save(f + '.jpg', 'JPEG', quality=90)

def drawEdges():
	for item in dirs:
	    if os.path.isfile(TARGET_FOLDER+item) and item != '.DS_Store':
	    	img = cv2.imread(TARGET_FOLDER+item) 
	    	edges = cv2.Canny(img, 100, 200) 
	    	cv2.imwrite(TARGET_FOLDER+item, edges) 

resize()