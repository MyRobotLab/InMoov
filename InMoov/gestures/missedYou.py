def missedYou():
  i01.startedGesture()
  #welcome   
  i01.setHandSpeed("left", 0.60, 0.60, 0.60, 0.60, 0.60, 0.60)
  i01.setHandSpeed("right", 0.60, 0.80, 0.60, 0.60, 0.60, 0.60)
  i01.setArmSpeed("left", 0.60, 0.60, 0.60, 0.60)
  i01.setArmSpeed("right", 0.60, 0.60, 0.60, 0.60)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(80,90)
  i01.moveArm("left",26,105,30,25)
  i01.moveArm("right",37,124,30,27)
  i01.moveHand("left",2,2,2,2,2,90)
  i01.moveHand("right",2,2,2,2,2,90)
  i01.mouth.speakBlocking("Oh, I missed you so much")
  sleep(2)
  #close arms
  chatBot.getResponse("SAY " + "Shall we give a hug")
  i01.finishedGesture()
 
def missedYouYes():
  i01.startedGesture()
  print "missed you yes"
  i01.moveHead(20,90,30)
  i01.moveArm("left",60,60,45,30)
  i01.moveArm("right",60,60,45,30)
  i01.moveHand("left",20,20,20,20,20,90)
  i01.moveHand("right",20,20,20,20,20,90)
  sleep(4)
  #remove arms
  i01.moveHead(20,90,30)
  i01.moveArm("left",71,94,41,31)
  i01.moveArm("right",71,94,41,31)
  i01.moveHand("left",20,20,20,20,20,90)
  i01.moveHand("right",20,20,20,20,20,90)
  sleep(2)
  #relax
  i01.moveHead(90,90,90)
  i01.moveArm("left",5,84,28,12)
  i01.moveArm("right",5,82,28,12)
  i01.moveHand("left",92,33,37,71,66,25)
  i01.moveHand("right",81,66,82,60,105,113)
  i01.moveTorso(95,90,90)
  i01.finishedGesture()
  
def missedYouNo():
  print "missed you no"
  relax()
