import numpy as np
import cv2
import os
cap = cv2.VideoCapture(0)
if(os.path.isdir('cam_frames')==False):
		os.mkdir('cam_frames')
directory = 'cam_frames'
count = 0
while(True):
	ret, frame = cap.read()
	cv2.imshow('frame',frame)
	cv2.imwrite(os.path.join(directory,"frame%s.jpg" % '{0:05}'.format(count)),frame) 
	count +=1
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
