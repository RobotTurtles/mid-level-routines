#
# Class for Facial Recognition
#
import cv2

class FaceRecognition:
	
	def __init__(self):
		self.webcam = cv2.VideoCapture(0)				
		
		self.frontalface = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")		# frontal face pattern detection
		
		self.Cface = [0,0]
		
	def FindFace(self, filename='default.jpg'):
			ret, img = self.webcam.read()
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
			faces = self.frontalface.detectMultiScale(gray, 1.3, 5)
			for (x,y,w,h) in faces:
				cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
				self.Cface = [(w/2+x),(h/2+y)]
    
			cv2.imwrite(filename, img)
			
			print str(self.Cface[0]) + "," + str(self.Cface[1])
			return self.Cface
