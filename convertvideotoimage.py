import cv2 
import sys
import os
def convertVedioToImage(path): 
    vidObj = cv2.VideoCapture(path) 
    count = 0
    success = 1
    directory = 'frames'
    while success: 
        success, image = vidObj.read() 
        cv2.imwrite(os.path.join(directory,"frame%s.jpg" % '{0:05}'.format(count)),image) 
        count += 1
    print("Total Frames:%d"%count)
if __name__ == '__main__':
	video = sys.argv[1]
	if(os.path.isdir('frames')==False):
		os.mkdir('frames')
	convertVedioToImage(video) 