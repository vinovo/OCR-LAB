from PIL import Image
import imagehash
import sys
import os

if len(sys.argv) != 2:
    sys.exit('Require target folder path: [folder_path]')

TARGET_FOLDER = sys.argv[1]
THRESHOLD = 6
numFilesRemoved = 0
GIF = '.gif'

def compareTwoImages(imageA, imageB):
	global numFilesRemoved

	hashA = imagehash.average_hash(Image.open(imageA))
	hashB = imagehash.average_hash(Image.open(imageB))

	diff = abs(hashA - hashB)
	if (diff < THRESHOLD):
		print("Images: " + imageA + "&" + imageB)
		print("Score: " + str(diff))
		#os.remove(imageB)
		numFilesRemoved += 1


initialNumFiles = len([name for name in os.listdir(TARGET_FOLDER) if os.path.isfile(TARGET_FOLDER + name)])

for first in os.listdir(TARGET_FOLDER):
	for second in os.listdir(TARGET_FOLDER):
		f = TARGET_FOLDER + first
		s = TARGET_FOLDER + second
		if ((GIF not in f) and (GIF not in s) and (f != s) and (os.path.isfile(f)) and (os.path.isfile(s))):
			compareTwoImages(f, s)

print("Initial number of files: " + str(initialNumFiles))
print("Files removed: " + str(numFilesRemoved))
print("Files remaining: " + str(initialNumFiles - numFilesRemoved))