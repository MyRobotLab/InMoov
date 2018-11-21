def takePicture():
  if not i01.opencv.isCapturing():
    i01.opencv.capture()
    i01.opencv.removeFilters()
    if flipPicture:i01.opencv.addFilter("Flip")
    photoFileName = opencv.recordFrame()
    print photoFileName
    AudioPlayer.playFile(RuningFolder+'/system/sounds/ShutterClik.mp3')
    imagedisplay.display(photoFileName)
  if i01.opencv.isCapturing():
    i01.opencv.removeFilters()
    if flipPicture:i01.opencv.addFilter("Flip")
    photoFileName = opencv.recordFrame()
    print photoFileName
    AudioPlayer.playFile(RuningFolder+'/system/sounds/ShutterClik.mp3')
    imagedisplay.display(photoFileName)
  sleep(10)
  imagedisplay.closeAll()
