#
# Class for Facial Recognition
#
import cv2

class FaceRecognition:
	
	def __init__(self):
		self.webcam = cv2.VideoCapture(0)				# Get ready to start getting images from the webcam
		self.webcam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 320)		# I have found this to be about the highest-
		self.webcam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 240)	# 	resolution you'll want to attempt on the pi
		
		frontalface = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")		# frontal face pattern detection
		profileface = cv2.CascadeClassifier("haarcascade_profileface.xml")		# side face pattern detection

		face = [0,0,0,0]	# This will hold the array that OpenCV returns when it finds a face: (makes a rectangle)
		Cface = [0,0]		# Center of the face: a point calculated from the above variable
		lastface = 0		# int 1-3 used to speed up detection. The script is looking for a right profile face,-
					# 	a left profile face, or a frontal face; rather than searching for all three every time,-
					# 	it uses this variable to remember which is last saw: and looks for that again. If it-
					# 	doesn't find it, it's set back to zero and on the next loop it will search for all three.-
					# 	This basically tripples the detect time so long as the face hasn't moved much.

	def FindFace(self):
			faceFound = False	# This variable is set to true if, on THIS loop a face has already been found
						# We search for a face three diffrent ways, and if we have found one already-
						# there is no reason to keep looking.
			
			if not faceFound:
				if self.lastface == 0 or self.lastface == 1:
					aframe = self.webcam.read()[1]	# there seems to be an issue in OpenCV or V4L or my webcam-
					aframe = self.webcam.read()[1]	# 	driver, I'm not sure which, but if you wait too long,
					aframe = self.webcam.read()[1]	#	the webcam consistantly gets exactly five frames behind-
					aframe = self.webcam.read()[1]	#	realtime. So we just grab a frame five times to ensure-
					aframe = self.webcam.read()[1]	#	we have the most up-to-date image.
					fface = self.frontalface.detectMultiScale(aframe,1.3,4,(cv2.cv.CV_HAAR_DO_CANNY_PRUNING + cv2.cv.CV_HAAR_FIND_BIGGEST_OBJECT + cv2.cv.CV_HAAR_DO_ROUGH_SEARCH),(60,60))
					if fface != ():			# if we found a frontal face...
						lastface = 1		# set lastface 1 (so next loop we will only look for a frontface)
						for f in fface:		# f in fface is an array with a rectangle representing a face
							faceFound = True
							self.face = f

			if not faceFound:				# if we didnt find a face yet...
				if lastface == 0 or lastface == 2:	# only attempt it if we didn't find a face last loop or if-
					aframe = self.webcam.read()[1]	# 	THIS method was the one who found it last loop
					aframe = self.webcam.read()[1]
					aframe = self.webcam.read()[1]	# again we grab some frames, things may have gotten stale-
					aframe = self.webcam.read()[1]	# since the frontalface search above
					aframe = self.webcam.read()[1]
					pfacer = self.profileface.detectMultiScale(aframe,1.3,4,(cv2.cv.CV_HAAR_DO_CANNY_PRUNING + cv2.cv.CV_HAAR_FIND_BIGGEST_OBJECT + cv2.cv.CV_HAAR_DO_ROUGH_SEARCH),(80,80))
					if pfacer != ():		# if we found a profile face...
						self.lastface = 2
						for f in pfacer:
							faceFound = True
							self.face = f

			if not faceFound:				# a final attempt
				if lastface == 0 or lastface == 3:	# this is another profile face search, because OpenCV can only-
					aframe = self.webcam.read()[1]	#	detect right profile faces, if the cam is looking at-
					aframe = self.webcam.read()[1]	#	someone from the left, it won't see them. So we just...
					aframe = self.webcam.read()[1]
					aframe = self.webcam.read()[1]
					aframe = self.webcam.read()[1]
					self.cv2.flip(aframe,1,aframe)	#	flip the image
					pfacel = self.profileface.detectMultiScale(aframe,1.3,4,(cv2.cv.CV_HAAR_DO_CANNY_PRUNING + cv2.cv.CV_HAAR_FIND_BIGGEST_OBJECT + cv2.cv.CV_HAAR_DO_ROUGH_SEARCH),(80,80))
					if pfacel != ():
						lastface = 3
						for f in pfacel:
							faceFound = True
							self.face = f

			if not faceFound:		# if no face was found...-
				self.lastface = 0		# 	the next loop needs to know
				self.face = [0,0,0,0]	# so that it doesn't think the face is still where it was last loop


			x,y,w,h = self.face
			Cface = [(w/2+x),(h/2+y)]	# we are given an x,y corner point and a width and height, we need the center
			print str(Cface[0]) + "," + str(Cface[1])
			return Cface
