def whataboutstarwars():
  if isNeopixelActivated:
    i01.setNeopixelAnimation("Ironman", 255, 255, 255, 1)
    sleep(3)
    i01.stopNeopixelAnimation()
  i01.startedGesture()
  x = (random.randint(1, 3))
  if x == 1:
      fullspeed()
      i01.moveHead(130,149,87,80,100)
      AudioPlayer.playFile(RuningFolder+'/system/sounds/R2D2.mp3')
      #i01.mouth.speak("R2D2")
      sleep(1)
      i01.moveHead(155,31,87,80,100)
      sleep(1)
      i01.moveHead(130,31,87,80,100)
      sleep(1)
      i01.moveHead(90,90,87,80,100)
      sleep(0.5)
      i01.moveHead(90,90,87,80,0)
      sleep(1)
      relax()
  if x == 2:
      fullspeed()
      #i01.mouth.speak("Hello sir, I am C3po unicyborg relations")
      AudioPlayer.playFile(RuningFolder+'/system/sounds/Hello sir, I am C3po unicyborg relations.mp3')
      i01.moveHead(138,80)
      i01.moveArm("left",79,42,23,41)
      i01.moveArm("right",71,40,14,39)
      i01.moveHand("left",180,180,180,180,180,47)
      i01.moveHand("right",99,130,152,154,145,180)
      i01.moveTorso(90,90,90)
      sleep(1)
      i01.moveHead(116,80)
      i01.moveArm("left",85,93,42,16)
      i01.moveArm("right",87,93,37,18)
      i01.moveHand("left",124,82,65,81,41,143)
      i01.moveHand("right",59,53,89,61,36,21)
      i01.moveTorso(90,90,90)
      sleep(1)
      relax()
  if x == 3:
      i01.setHandSpeed("left", 43.0, 43.0, 43.0, 43.0, 43.0, 100.0)
      i01.setHandSpeed("right", 100.0, 43.0, 100.0, 100.0, 100.0, 100.0)
      i01.setArmSpeed("left", 100.0, 100.0, 100.0, 100.0)
      i01.setArmSpeed("right", 50, 100.0, 100.0, 100.0)
      i01.setHeadSpeed(100.0, 50)
      i01.setTorsoSpeed(100.0, 100.0, 100.0)
      i01.moveHead(80,86)
      i01.moveArm("left",5,94,30,10)
      i01.moveArm("right",7,74,50,10)
      i01.moveHand("left",180,180,180,180,180,90)
      i01.moveHand("right",180,2,175,160,165,180)
      i01.moveTorso(90,90,90)
      #i01.mouth.speak("mmmmmmh, from the dark side you are")
      AudioPlayer.playFile(RuningFolder+'/system/sounds/mmmmmmh, from the dark side you are.mp3')
      sleep(4.5)
  i01.finishedGesture()
  relax()
