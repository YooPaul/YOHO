# adapted from: https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/ 

# USAGE
# python facial_landmarks.py --shape-predictor shape_predictor_68_face_landmarks.dat --image images/example_01.jpg 

# import the necessary packages
from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2
import os

# construct the argument parser and parse the arguments

def getFacialLandmarks(directory, shape_predictor):
	directory = os.fsencode(directory)

	print("Initializing...")
	# initialize dlib's face detector (HOG-based) and then create
	# the facial landmark predictor
	detector = dlib.get_frontal_face_detector()
	predictor = dlib.shape_predictor(shape_predictor)

	print("\nRemoving old files...")

	number = len(os.listdir(directory))
	print("%d files in total" % number)
	counter = 0

	for file in os.listdir(directory):
		filename = os.fsdecode(file)
		if filename.endswith(".txt"):
			open(os.fsdecode(directory) + "/" + filename, "w")

	print("\nFinding mouths...")

	for file in os.listdir(directory):
		filename = os.fsdecode(file)
		if filename.endswith(".jpg"):
			print("%f%% done" % ((counter / number) * 100))
			# print(str(counter))
			# load the input image, resize it, and convert it to grayscale
			image = cv2.imread(os.fsdecode(directory) + "/" + filename)
			if image is None:
				continue
			image = imutils.resize(image, width=500)
			gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			# detect faces in the grayscale image
			rects = detector(gray, 1)

			for (i, rect) in enumerate(rects):
				# determine the facial landmarks for the face region, then
				# convert the facial landmark (x, y)-coordinates to a NumPy
				# array
				shape = predictor(gray, rect)
				shape = face_utils.shape_to_np(shape)

				# loop over the (x, y)-coordinates for the mouth and find
				# a bounding box
				min_x = 500
				max_x = 0
				min_y = 0x7fffffff
				max_y = -0x80000000

				for i in range(48, 68):
					(x, y) = tuple(shape[i])
					min_x = min(min_x, x)
					max_x = max(max_x, x)
					min_y = min(min_y, y)
					max_y = max(max_y, y)

				width = max_x - min_x
				height = max_y - min_y
				# cv2.rectangle(image, (min_x, min_y), (max_x, max_y), (0, 255, 0), 2)

				# write the bounding box to a file
				# f = open(os.fsdecode(directory) + "/" + filename.replace(".jpg", ".txt"), "w")
				f = open(os.fsdecode(directory) + "/" + filename.replace(".jpg", ".txt"), "a")
				f.write(str(min_x) + " " + str(min_y) + " " + str(width) + " " + str(height) + "\n")
				f.close()

				# cv2.imshow("Output", image)
				# cv2.waitKey(0)
		counter += 1

if __name__ == "__main__":
	ap = argparse.ArgumentParser()
	ap.add_argument("-p", "--shape-predictor", required=True,
		help="path to facial landmark predictor")
	ap.add_argument("-d", "--directory", required=True,
		help="path to directory with input images")
	args = vars(ap.parse_args())
	getFacialLandmarks(args["directory"], args["shape_predictor"])


# load the input image, resize it, and convert it to grayscale
# image = cv2.imread(args["image"])
# image = imutils.resize(image, width=500)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # detect faces in the grayscale image
# rects = detector(gray, 1)

# # loop over the face detections
# for (i, rect) in enumerate(rects):
# 	# determine the facial landmarks for the face region, then
# 	# convert the facial landmark (x, y)-coordinates to a NumPy
# 	# array
# 	shape = predictor(gray, rect)
# 	shape = face_utils.shape_to_np(shape)

# 	# convert dlib's rectangle to a OpenCV-style bounding box
# 	# [i.e., (x, y, w, h)], then draw the face bounding box
# 	(x, y, w, h) = face_utils.rect_to_bb(rect)
# 	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# 	# show the face number
# 	cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
# 		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# 	# loop over the (x, y)-coordinates for the facial landmarks
# 	# and draw them on the image
# 	for (x, y) in shape:
# 		cv2.circle(image, (x, y), 1, (0, 0, 255), -1)

# show the output image with the face detections + facial landmarks
