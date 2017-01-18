def stopfacerecognizer():
	i01.opencv.removeCapture()
	i01.opencv.removeFilter("PyramidDown")
	i01.opencv.removeDisplayFilter("FaceRecognizer")