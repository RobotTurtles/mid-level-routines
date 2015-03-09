#
# Class for Facial Recognition
#
import cv2
import datetime
import logging
		
class FaceRecognition:
	
	def __init__(self, logger):
		self.logger = logger
		#self.webcam = cv2.VideoCapture(0)
		self.frontalface = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
		self.Cface = [0,0,0]
		
	def FindFace(self, filename='lastFaceFound.jpg', capturePath='captures', missedPath='misses'):
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
				filename = capturePath + '/' + datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S.jpg")
				self.logger.info(filename)
				cv2.imwrite(filename, img)
			
		if(self.Cface[2] == 0):
			filename = missedPath + '/' + datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S.jpg")	
			self.logger.info(filename)
			cv2.imwrite(filename, img)
			
		self.logger.info(str(self.Cface[0]) + "," + str(self.Cface[1]) + ",width:"+ str(self.Cface[2]))
		self.webcam.release()	
		return self.Cface
