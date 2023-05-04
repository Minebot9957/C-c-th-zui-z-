import threading
import winsound

import cv2
import imutils


cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

_, start_frame = cap.read()
start_frame = imutils.resize(start_frame, width=500)
start_frame = cv2.cvtColor(start_frame, cv2.COLOR_BGR2GRAY)
start_frame = cv2.GaussianBlur(start_frame, (21,21), 0)\

arlam = False 
arlam_mode = False
arlam_counter = 0


def beep_alarm():
	global arlam
	for _ in range(5):
		if not arlam_mode:
			break
		print ("ALARM")
		winsound.Beep(2500, 1000)
	arlam = False


while True:

		_, frame = cap.read()
		frame = imutils.resize(frame, width=500)

		if arlam_mode:
			frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			frame_bw = cv2.GaussianBlur(frame_bw, (5, 5), 0)

			difference = cv2.absdiff(frame_bw, start_frame)
			threshold = cv2.threshold(difference ,25, 255, cv2.THRESH_BINARY)[1]
			start_frame = frame_bw 

			if threshold.sum() > 1000:
				arlam_counter += 1
			else:
				if arlam_counter > 0:
					arlam_counter -= 1
				
			cv2.imshow("Camera", threshold)
	    
		else:	
			cv2.imshow("Camera", frame)

		if arlam_counter > 10:
			if not arlam :
				arlam = True
				threading.Thread(target=beep_alarm).start()

		key_pressed = cv2.waitKey(30)
		if key_pressed == ord("t"):
			arlam_mode = not arlam_mode
			arlam_counter = 0
		if key_pressed == ord("q"):
			arlam_mode = False
			break

cap.release()
cv2.destroyAllWindows()		        	            					            				