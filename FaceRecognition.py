#
# Class for Facial Recognition
#
import numpy as np
import cv2
import datetime
import logging
import time
import math

class FaceRecognition:
	
	def __init__(self, logger):
		self.logger = logger
		self.frontalface = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
		self.webcam = cv2.VideoCapture(0)
		self.logFrames = True
		self.face = None
		self.cface = [0,0,0]
		self.features = None
		self.hasFace = False
		self.lastGray = None
		self.frameCount = 0
		
	def FindFace(self, filename='lastFaceFound.jpg', capturePath='captures', missedPath='misses'):
		startTime = time.time()

		self.frameCount += 1
		
		ret, img = self.webcam.read()
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

		newImage = False
		if self.lastGray != None:
			(h,w) = gray.shape
			diff = cv2.absdiff(self.lastGray, gray).sum() / (h*w)
			if diff > 1.0:
				newImage = True

		if newImage:
			# periodically redetect
			if self.frameCount % 120 == 0:
				self.hasFace = False
		
			if not (self.hasFace and self.lastGray != None):
				# find a face
				# TODO: if we don't find one, don't keep searching. wait for some other image change.
				self.face = None
				self.cface = [0,0,0]
				self.hasFace = False
				self.logger.info("Looking for a new face")
				faces = self.frontalface.detectMultiScale(gray, 1.3, 5, flags = cv2.CASCADE_FIND_BIGGEST_OBJECT)
				if len(faces) > 0:
					self.logger.info("Found one")
					self.face = faces[0]
					(x,y,w,h) = self.face
					self.cface = [(w/2+x),(h/2+y),w]

					faceImage = gray[y:y+h, x:x+w]
					self.features = cv2.goodFeaturesToTrack(faceImage, 100, 0.01, 20)
					self.features += [x,y]
					self.hasFace = True
			else:
				# follow the points
				self.logger.info("Tracking an existing face")
				nextFeatures, status, err = cv2.calcOpticalFlowPyrLK(self.lastGray, gray, self.features)
				calcPrevFeatures, status, err = cv2.calcOpticalFlowPyrLK(gray, self.lastGray, nextFeatures)
				d = abs(self.features-calcPrevFeatures).reshape(-1, 2).max(-1)
				good = d < 1
				goodFeatures = self.features[good]
				if len(goodFeatures) >= 10:
					self.features = goodFeatures
					nextFeatures = nextFeatures[good]
				self.face = self.predictBB(img, self.face, self.features, nextFeatures, good)
				(x,y,w,h) = self.face
				self.cface = [(w/2+x),(h/2+y),w]
				self.features = nextFeatures

			# (x,y,w,h) = self.face
			# faceImage = gray[y:y+h, x:x+w]
			# self.features = cv2.goodFeaturesToTrack(faceImage, 25, 0.01, 10)
			# self.features += [x,y]
		else:
			self.logger.info("No change.")
			
		if self.logFrames:
			if self.face != None:
				(x,y,w,h) = self.face
				cv2.rectangle(img,(int(x),int(y)),(int(x)+int(w),int(y)+int(h)),(255,0,0),2)
			cv2.imshow('image', img)

		self.lastGray = gray
		
		return self.cface

	def predictBB(self, img, bb0, pt0, pt1, good):
		deltas = (pt1 - pt0)
		dxsum = 0.0
		dysum = 0.0
		count = 0
		minThresh = 1.0
		x0 = []
		y0 = []
		x1 = []
		y1 = []
		for d,t0,t1,good in zip(deltas, pt0, pt1, good):
			dx,dy = d.ravel()
			t0x, t0y = t0.ravel()
			t1x, t1y = t1.ravel()
#			if not good:
#				cv2.circle(img,(t1x,t1y),3,(0,0,255),-1)
#				continue
			movement = math.sqrt(dx**2 + dy**2)
			if movement < minThresh:
				# the point didn't move. don't count it.
				cv2.circle(img,(t1x,t1y),3,(0,255,0),-1)
				continue
			cv2.circle(img,(t1x,t1y),3,(255,0,0),-1)
			dxsum += dx
			dysum += dy
			count += 1
			x0.append(t0x)
			y0.append(t0y)
			x1.append(t1x)
			y1.append(t1y)
		
		if count == 0:
			return bb0
		else:
			cen_dx = dxsum / count
			cen_dy = dysum / count

			A = np.array([x0 + cen_dx, np.ones(len(x0))])
			w = np.linalg.lstsq(A.T, x1)[0]
			xscal = w[0]

			# A = np.array([y0 + cen_dy, np.ones(len(y0))])
			# w = np.linalg.lstsq(A.T, y1)[0]
			# yscal = w[0]

			bb = [bb0[0]+cen_dx, bb0[1]+cen_dy, bb0[2] * xscal, bb0[3] * xscal]
			
			return bb

	def __del__(self):
   	        if self.webcam:
			self.webcam.release()
		    
	    
