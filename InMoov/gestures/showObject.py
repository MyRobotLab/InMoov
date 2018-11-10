#waiting IK, we script 3 positions to point 3 objects on the table
#so, here we assume there are only 3 possibles positions for output

def showObject(position):
  i01.halfSpeed()
  if position==1:showToLeft()
  if position==2:showToCenter()
  if position>=3:showToRight()

def showToCenter():
  i01.moveHead(0.00,90.20,95.00,90.00,0.00,90.20)
  i01.moveArm("left",0.20,90.20,30.20,10.00)
  i01.moveArm("right",71.00,69.00,58.00,24.00)
  i01.moveHand("left",80.00,80.00,80.00,80.00,80.00,14.00)
  i01.moveHand("right",180.00,0.00,180.00,180.00,180.00,180.00)
  i01.moveTorso(90.20,90.20,90.00)
  
def showToLeft():
  i01.moveHead(90.00,100.00,90.00,90.00,0.00,90.00)
  i01.moveArm("left",48.00,94.00,63.00,18.00)
  i01.moveArm("right",5.00,82.00,28.00,15.00)
  i01.moveHand("left",180.00,32.00,180.00,180.00,180.00,0.00)
  i01.moveHand("right",80.00,80.00,80.00,80.00,80.00,180.00)
  i01.moveTorso(95.00,90.00,90.00)
  
def showToRight():
  i01.moveHead(41.00,86.00,90.00,90.00,0.00,90.20)
  i01.moveArm("left",0.20,84.00,28.00,10.00)
  i01.moveArm("right",65.00,82.00,58.00,10.00)
  i01.moveHand("left",80.00,80.00,80.00,80.00,80.00,28.00)
  i01.moveHand("right",180.00,0.00,180.00,180.00,180.00,180.00)
  i01.moveTorso(82.00,85.00,91.00)
