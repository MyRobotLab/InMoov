# ##############################################################################
#            *** FROM InMoov3.minimalArm.py ***
# ##############################################################################

def rightbicepsraise():
  i01.moveArm("right",180,80,0,0)

def rightbicepslower():
  i01.moveArm("right",0,80,0,0)
  
def leftbicepsraise():
  i01.moveArm("left",180,80,0,0)

def leftbicepslower():
  i01.moveArm("left",0,80,0,0)
  
def omoplate():
  i01.moveArm("left",0,0,0,180)
  i01.moveArm("right",0,0,0,180)
