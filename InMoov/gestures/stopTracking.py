def stopTracking():
  if (i01.RobotIsOpenCvCapturing()):
    i01.headTracking.stopTracking()
    i01.eyesTracking.stopTracking()
    i01.finishedGesture()

