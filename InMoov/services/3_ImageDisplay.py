# ##############################################################################
#                 ImageDisplay SERVICE
# ##############################################################################

# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

ImageDisplay=Runtime.createAndStart("ImageDisplay", "ImageDisplay")

def displayPic(pic):
  if not virtualInmoovAlwaysActivated and not ScriptType=="Virtual":
    r=ImageDisplay.displayFullScreen(pic)