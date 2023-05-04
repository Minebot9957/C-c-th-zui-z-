import cv2
from PIL import Image

from pytesseract import pytesseract, Output
#cac ham
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
myconfig = r"--psm 11 --oem 3"   
#chupanhtucam
while True:
	_,image=camera.read()
	cv2.imshow('Text',image)
	if cv2.waitKey(1)& 0xFF==ord('s'):
		cv2.imwrite('test1.jpg',image)
		break
camera.release()
cv2.destroyAllWindows()

def tesseract():
	path=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
	imagepath='test1.jpg'
	pytesseract.tesseract_cmd=path
	text=pytesseract.image_to_string(Image.open(imagepath), lang="vie")
	print(text[:-1])
tesseract()
	
	#boxes = pytesseract.image_to_boxes(img, config=myconfig)
	#for box in boxes.splitlines():
	#	box = box.split(" ")
	#	img = cv2.rectangle(img, (int(box[1]), height - int(box[2])),(int(box[3]), height - int(box[4])),(0, 255, 0), 2)
	
#height, width, _ = img.shape

#data = pytesseract.image_to_data(img, config=myconfig, output_type=Output.DICT)

#amount_boxes = len(data['text'])
#for i in range(amount_boxes):
	#if float(data['conf'][i]) > 80:
		#(x, y, width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
		#img = cv2.rectangle(img, (x, y), (x+width, y+height), (0,255,0), 2)
		#img = cv2.putText(img, data['text'][i], (x, y+height+20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0),2,cv2.LINE_AA)
	#cv2.imshow("test", img)
	#cv2.waitKey(0)


	