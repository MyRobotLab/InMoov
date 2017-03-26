# ##############################################################################
#            *** FROM InMoov3.minimal.py ***
# ##############################################################################

def handsopen():
  i01.moveHand("left",0,0,0,0,0)
  i01.moveHand("right",0,0,0,0,0)
  
def handsclose():
  i01.moveHand("left",180,180,180,180,180)
  i01.moveHand("right",180,180,180,180,180)
  
def righthandopen():
  i01.moveHand("right",0,0,0,0,0)


def righthandclose():
  i01.moveHand("right",180,180,180,180,180)

def lefthandopen():
  i01.moveHand("left",0,0,0,0,0)


def lefthandclose():
  i01.moveHand("left",180,180,180,180,180)
  
def handopen():
  righthandopen()

def handclose():
  righthandclose()