#
# Class for Facial Recognition
#
import cv2
import datetime

class FaceRecognition:
	
	def __init__(self):
		#self.webcam = cv2.VideoCapture(0)				
		
		self.frontalface = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")		# frontal face pattern detection
		
		self.Cface = [0,0,0]
		
	def FindFace(self, filename='lastFaceFound.jpg'):
			self.Cface = [0,0,0]
			self.webcam = cv2.VideoCapture(0)	
			ret, img = self.webcam.read()
			ret, img = self.webcam.read()	
			ret, img = self.webcam.read()
			ret, img = self.webcam.read()
			ret, img = self.webcam.read()
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
			faces = self.frontalface.detectMultiScale(gray, 1.3, 5)
			for (x,y,w,h) in faces:
				cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
				self.Cface = [(w/2+x),(h/2+y),w]
			
				if(x != 0 and y != 0):
					filename = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S.jpg")	
					print filename	
					cv2.imwrite(filename, img)
			
			print str(self.Cface[0]) + "," + str(self.Cface[1]) + ",width:"+ str(self.Cface[2])
			self.webcam.release()	
			return self.Cface
