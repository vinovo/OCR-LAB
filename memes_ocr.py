import subprocess
import sys
import os

if len(sys.argv) != 2:
    sys.exit('Require target folder path: [folder_path]')

TARGET_FOLDER = sys.argv[1]

def translate(image):
	process = subprocess.Popen(['./MemesOCR', image], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stdout, stderr = process.communicate()
	print(image)
	print(stdout.decode('utf-8'))

for first in os.listdir(TARGET_FOLDER):
	f = TARGET_FOLDER + first
	if (os.path.isfile(f)):
		translate(f)
