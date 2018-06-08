def missedYou():
  inMoov.startedGesture()
  #welcome   
  inMoov.setHandVelocity("left", 19, 19, 19, 19, 19, 19)
  inMoov.setHandVelocity("right", 19, 36, 19, 19, 19, 19)
  inMoov.setArmVelocity("left", 19, 19, 19, 19)
  inMoov.setArmVelocity("right", 19, 19, 19, 19)
  inMoov.setHeadVelocity(22.0, 22.0)
  inMoov.moveHead(80,90)
  inMoov.moveArm("left",26,105,30,25)
  inMoov.moveArm("right",37,124,30,27)
  inMoov.moveHand("left",2,2,2,2,2,90)
  inMoov.moveHand("right",2,2,2,2,2,90)
  inMoov.mouth.speakBlocking("Oh, I missed you so much")
  sleep(2)
  #close arms
  chatBot.getResponse("SAY " + "Shall we give a hug")
  inMoov.finishedGesture()
 
def missedYouYes():
  inMoov.startedGesture()
  print "missed you yes"
  inMoov.moveHead(20,90,30)
  inMoov.moveArm("left",60,60,45,30)
  inMoov.moveArm("right",60,60,45,30)
  inMoov.moveHand("left",20,20,20,20,20,90)
  inMoov.moveHand("right",20,20,20,20,20,90)
  sleep(4)
  #remove arms
  inMoov.moveHead(20,90,30)
  inMoov.moveArm("left",71,94,41,31)
  inMoov.moveArm("right",71,94,41,31)
  inMoov.moveHand("left",20,20,20,20,20,90)
  inMoov.moveHand("right",20,20,20,20,20,90)
  sleep(2)
  #relax
  inMoov.moveHead(90,90,90)
  inMoov.moveArm("left",5,84,28,12)
  inMoov.moveArm("right",5,82,28,12)
  inMoov.moveHand("left",92,33,37,71,66,25)
  inMoov.moveHand("right",81,66,82,60,105,113)
  inMoov.moveTorso(95,90,90)
  inMoov.finishedGesture()
  
def missedYouNo():
  print "missed you no"
  relax()
