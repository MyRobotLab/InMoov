def darknet():  
  imagedisplay.closeAll()
  sleep(0.5)
  if isNeopixelActivated==1:
        i01.setNeopixelAnimation("Color Wipe", 25, 5, 10, 15)
  if isOpenCvActivated==1:  
    if i01.RobotIsOpenCvCapturing():
      i01.setHeadVelocity(-1,-1,-1,-1,-1,-1)
      i01.moveHeadBlocking(75,90,90,30,0,90)
      sleep(1)
      takeFotoForYolo()
      statisticResult()
      sleep(0.1)
      analyseResult()
    else:
      i01.opencv.capture()
      sleep(1)
      i01.setHeadVelocity(-1,-1,-1,-1,-1,-1)
      i01.moveHeadBlocking(75,90,90,30,0,90)
      sleep(1)
      takeFotoForYolo()
      statisticResult()
      sleep(0.1)
      analyseResult()
