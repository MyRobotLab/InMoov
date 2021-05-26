
def YoloOnUSonic():
  i01.setHeadSpeed(100.0,100.0,100.0,100.0,100.0,100.0)
  if ultraSonicSensorActivated:
    distance=200
    timeout=0
    timeoutGetCloser=0
    while (not distance or distance > 100): 
      timeout+=1
      timeoutGetCloser+=1
      distance=i01.getUltrasonicRightDistance()
      print distance
      if timeout > 20:
        i01.chatBot.getResponse("SYSTEM_NO_OBJECT")
        sleep(1)
        break
      # ask to move object CLOSER
      if timeoutGetCloser>6:
        i01.chatBot.getResponse("SYSTEM_GET_OBJECT_CLOSER")
        timeoutGetCloser=0
        sleep(1)
      sleep(0.5)
      # Nice an object is detected
    if distance<=100:
      i01.chatBot.getResponse("SYSTEM_SEE_OBJECT")
      sleep(1)
  else:
    sleep(1)
    No()
    i01.speakBlocking("I think my Ultrasonic is not activated")
