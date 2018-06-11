# -- coding: utf-8 --
# ##############################################################################
#						*** INMOOV MINIMAL ***
# 			  Those actions are inside inmoovGestures
# ##############################################################################

#to translate

# GENERAL
ear.addCommand(u"disconnect everything", "python", "disableAll()")
ear.addCommand(u"rest", "python", "rest")
ear.addCommand(u"list", "python", "rest")
ear.addCommand(u"first", "python", "rest")

# ARM((S) - inmoovGestures\ minimalArm.py
ear.addCommand(u"disconnect left arm", "i01.leftArm", "disable")
ear.addCommand(u"raise your right bicep", "python", "rightbicepsraise")
ear.addCommand(u"lower your right bicep", "python", "rightbicepslower")
ear.addCommand(u"raise your left bicep", "python", "leftbicepsraise")
ear.addCommand(u"lower your left bicep", "python", "lefttbicepslower")
ear.addCommand(u"arms front", "python", "armsFront")
ear.addCommand(u"da vinci", "python", "daVinci")
ear.addCommand(u"davinci", "python", "daVinci")
ear.addCommand(u"omoplate", "python", "omoplate")

# HAND(S) - inmoovGestures\ minimalHand.py
ear.addCommand(u"open your hands", "python", "handsopen")
ear.addCommand(u"close your hands", "python", "handsclose")
ear.addCommand(u"open your right hand", "python", "handopen")
ear.addCommand(u"close your right hand", "python", "handclose")
ear.addCommand(u"open your hand", "python", "handopen")
ear.addCommand(u"close your hand", "python", "handclose")
ear.addCommand(u"open your left hand", "python", "lefthandopen")
ear.addCommand(u"close your left hand", "python", "lefthandclose")

# HEAD - inmoovGestures\ minimalHead.py
ear.addCommand(u"disconnect head", "i01.head", "disable")
ear.addCommand(u"disconnect eyes", "i01.head.eyeY", "disable")
ear.addCommand(u"look on your right side", "python", "lookrightside")
ear.addCommand(u"look on your left side", "python", "lookleftside")
ear.addCommand(u"look in the middle", "python", "lookinmiddle")
ear.addCommand(u"search humans", "python", "trackHumans")
ear.addCommand(u"quit search", "python", "stopTracking")
ear.addCommand(u"track", "python", "trackPoint")
ear.addCommand(u"freeze track", "python", "stopTracking")
ear.addCommand(u"tilt head to the left", "python", "tiltHeadLeftSide")
ear.addCommand(u"tilt head to the right", "python","tiltHeadRightSide")

# TORSO - inmoovGestures\minimalTorso.py
ear.addCommand("disconnect torso", "i01.torso", "disable")
ear.addCommand("test your stomach", "python", "teststomach")
