def facerecognizer(): 
  #you need to train at least 2 FACES !   
  i01.cameraOn()
  fr=i01.vision.setActiveFilter("FaceRecognizer")
  fr.setMode(OpenCVFilterFaceRecognizer.Mode.TRAIN)
  fr.train()# it takes some time to train and be able to recognize face
  fr.setMode(OpenCVFilterFaceRecognizer.Mode.RECOGNIZE)
