#waiting IK, we script 3 positions to point 3 objects on the table
#so, here we assume there are only 3 possibles positions for output

def showObject(position):
  i01.halfSpeed()
  if position==1:showToLeft()
  if position==2:showToCenter()
  if position>=3:showToRight()

def showToCenter():
  i01.moveHead(0.00,90.20,90.00,90.00,0.00,90.20)
  i01.moveArm("left",0.20,90.20,30.20,10.00)
  i01.moveArm("right",114.00,53.00,58.00,34.00)
  i01.moveHand("left",0.00,0.00,180.00,0.00,0.00,90.20)
  i01.moveHand("right",180.00,0.00,180.00,180.00,0.00,180.00)
  i01.moveTorso(90.20,90.20,90.00)
  
def showToLeft():
  i01.moveHead(0.00,115.00,90.00,90.00,0.00,90.20)
  i01.moveArm("left",0.20,90.20,30.20,10.00)
  i01.moveArm("right",127.00,63.00,60.00,13.00)
  i01.moveHand("left",0.00,0.00,180.00,0.00,0.00,90.20)
  i01.moveHand("right",180.00,0.00,180.00,180.00,0.00,180.00)
  i01.moveTorso(126.00,162.00,90.00)
  
def showToRight():
  i01.moveHead(0.00,66.00,90.00,90.00,0.00,90.20)
  i01.moveArm("left",0.20,90.20,30.20,10.00)
  i01.moveArm("right",135.00,82.00,39.00,0.00)
  i01.moveHand("left",0.00,0.00,180.00,0.00,0.00,90.20)
  i01.moveHand("right",180.00,0.00,180.00,180.00,0.00,180.00)
  i01.moveTorso(82.00,62.00,91.00)