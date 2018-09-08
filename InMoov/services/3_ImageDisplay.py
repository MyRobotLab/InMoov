# ##############################################################################
#                 ImageDisplay SERVICE
# ##############################################################################

# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

imagedisplay = Runtime.start("imagedisplay","ImageDisplay")

def displayPic(pic):
  imagedisplay.closeAll()
  r=imagedisplay.displayFullScreen(pic)
