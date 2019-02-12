import cv2
from os import listdir
from os import path
import sys
video_name = 'output.avi'
image_folder = 'frames'
images = []

try:
	fps = int(sys.argv[1])
except IndexError: 
	print("ERROR:Input Required FPS")
	exit()

for img in sorted(listdir(image_folder)):
	images.append(img)

frame = cv2.imread(path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, fps, (width,height))

for image in images:
    video.write(cv2.imread(path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()