# ##############################################################################
#						*** INMOOV MINIMAL ***
#				** INMOUV CONTROL WITHOUT CHATBOT **
#** LOOK INSIDE INMOOVSKELETON FOLDER ABOUT SKELETON SPECIFIC PART **
# ##############################################################################

# this is merge about gael mnimal ( left+right )

# general
ear.addCommand("attach everything", "i01", "attach")
ear.addCommand("disconnect everything", "i01", "detach")
ear.addCommand("capture gesture", ear.getName(), "captureGesture")
# InMoov3.minimalArm.py
ear.addCommand("arms front", i01.getName(), "armsFront")
ear.addCommand("da vinci", i01.getName(), "daVinci")
# InMoov3.minimal.py
ear.addCommand("open your hands", "python", "handsopen")
ear.addCommand("close your hands", "python", "handsclose")
ear.addCommand("rest", "python", "rest")

def rest():
	if RightPortIsConnected:
		i01.moveHand("right",0,0,0,0,0)
		i01.moveArm("right",5,90,30,10)
	
	
	if LeftPortIsConnected:
		i01.moveHand("left",0,0,0,0,0)
		i01.moveArm("left",5,90,30,10)

def handsopen():
	i01.moveHand("left",0,0,0,0,0)
	i01.moveHand("right",0,0,0,0,0)
	
def handsclose():
	i01.moveHand("left",180,180,180,180,180)
	i01.moveHand("right",180,180,180,180,180)