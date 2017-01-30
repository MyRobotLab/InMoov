# ##############################################################################
#						*** INMOOV MINIMAL ***
# 			  Those actions are inside inmoovGestures
# ##############################################################################


# GENERAL
ear.addCommand("attach everything", "i01", "attach")
ear.addCommand("disconnect everything", "i01", "detach")
ear.addCommand("rest", "python", "rest")
ear.addCommand("list", "python", "rest")
ear.addCommand("first", "python", "rest")
ear.addCommand("gesture test", "python", "gestureTEST")

# ARM((S) - inmoovGestures\ minimalArm.py
ear.addCommand("attach left arm", "i01.leftArm", "attach") #to remove soon
ear.addCommand("disconnect left arm", "i01.leftArm", "detach") #to remove soon
ear.addCommand("raise your right bicep", "python", "rightbicepsraise")
ear.addCommand("lower your right bicep", "python", "rightbicepslower")
ear.addCommand("raise your left bicep", "python", "leftbicepsraise")
ear.addCommand("lower your left bicep", "python", "lefttbicepslower")
ear.addCommand("arms front", "i01.getName()", "armsFront")
ear.addCommand("da vinci", "i01.getName()", "daVinci")
ear.addCommand("davinci", "i01.getName()", "daVinci")
ear.addCommand("omoplate", "python", "omoplate")

# HAND(S) - inmoovGestures\ minimalHand.py
ear.addCommand("open your hands", "python", "handsopen")
ear.addCommand("close your hands", "python", "handsclose")
ear.addCommand("open your right hand", "python", "handopen")
ear.addCommand("close your right hand", "python", "handclose")
ear.addCommand("open your hand", "python", "handopen")
ear.addCommand("close your hand", "python", "handclose")
ear.addCommand("open your left hand", "python", "lefthandopen")
ear.addCommand("close your left hand", "python", "lefthandclose")

# HEAD - inmoovGestures\ minimalHead.py
ear.addCommand("attach head", "i01.head", "attach")
ear.addCommand("disconnect head", "i01.head", "detach")
ear.addCommand("attach eyes", "i01.head.eyeY", "attach")
ear.addCommand("disconnect eyes", "i01.head.eyeY", "detach")
ear.addCommand("look on your right side", "python", "lookrightside")
ear.addCommand("look on your left side", "python", "lookleftside")
ear.addCommand("look in the middle", "python", "lookinmiddle")


