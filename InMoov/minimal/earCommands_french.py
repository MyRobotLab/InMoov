# -- coding: utf-8 --
# ##############################################################################
#						*** INMOOV MINIMAL FRENCH ***
# 			  Those actions are inside inmoovGestures
# ##############################################################################


# GENERAL
ear.addCommand(u"désactiver tout", "python", "disableAll()")
ear.addCommand(u"repos", "python", "rest")

# ARM((S) - inmoovGestures\minimalArm.py
ear.addCommand(u"détacher le bras gauche", "i01.leftArm", "disable")
ear.addCommand(u"lève le biceps droit", "python", "rightbicepsraise")
ear.addCommand(u"baisse le biceps droit", "python", "rightbicepslower")
ear.addCommand(u"lève le biceps gauche", "python", "leftbicepsraise")
ear.addCommand(u"baisse le biceps gauche", "python", "lefttbicepslower")
ear.addCommand(u"bras devant", "python", "armsFront")
ear.addCommand(u"da vinci", "python", "daVinci")
ear.addCommand(u"omoplate", "python", "omoplate")

# HAND(S) - inmoovGestures\minimalHand.py
ear.addCommand(u"ouvre les mains", "python", "handsopen")
ear.addCommand(u"ferme les mains", "python", "handsclose")
ear.addCommand(u"ouvre la main droite", "python", "handopen")
ear.addCommand(u"ferme la main droite", "python", "handclose")
ear.addCommand(u"ouvre la main", "python", "handopen")
ear.addCommand(u"ferme la main", "python", "handclose")
ear.addCommand(u"ouvre la main gauche", "python", "lefthandopen")
ear.addCommand(u"ferme la main gauche", "python", "lefthandclose")

# HEAD - inmoovGestures\minimalHead.py
ear.addCommand(u"détacher la tête", "i01.head", "disable")
ear.addCommand(u"détacher les yeux", "i01.head.eyeY", "disable")
ear.addCommand(u"regarde sur ta droite", "python", "lookrightside")
ear.addCommand(u"regarde sur ta gauche", "python", "lookleftside")
ear.addCommand(u"regarde au milieu", "python", "lookinmiddle")
ear.addCommand(u"cherche un humain", "python", "trackHumans")
ear.addCommand(u"arrête de chercher", "python", "stopTracking")
ear.addCommand(u"suis du regard ce point", "python", "trackPoint")
ear.addCommand(u"arrête de suivre du regard", "python", "stopTracking")
ear.addCommand(u"penche la tête à gauche", "python", "tiltHeadLeftSide")
ear.addCommand(u"penche la tête à droite", "python","tiltHeadRightSide")

# TORSO - inmoovGestures\minimalTorso.py
ear.addCommand(u"détacher le torse", "i01.torso", "disable")
ear.addCommand(u"test torse", "python", "teststomach")

