# -- coding: utf-8 --
# ##############################################################################
#						*** INMOOV MINIMAL FRENCH ***
# 			  Those actions are inside inmoovGestures
# ##############################################################################


# GENERAL
ear.addCommand(u"attacher tout", "i01", "attach")
ear.addCommand(u"détacher tout", "python", "detachAll()")
ear.addCommand(u"repos", "python", "rest")

# ARM((S) - inmoovGestures\_minimalArm.py
ear.addCommand(u"attacher le bras gauche", "i01.leftArm", "attach") #to remove soon
ear.addCommand(u"détacher le bras gauche", "i01.leftArm", "detach") #to remove soon
ear.addCommand(u"lève le biceps droit", "python", "rightbicepsraise")
ear.addCommand(u"baisse le biceps droit", "python", "rightbicepslower")
ear.addCommand(u"lève le biceps gauche", "python", "leftbicepsraise")
ear.addCommand(u"baisse le biceps gauche", "python", "lefttbicepslower")
ear.addCommand(u"bras devant", i01.getName(), "armsFront")
ear.addCommand(u"da vinci", i01.getName(), "daVinci")
ear.addCommand(u"omoplate", "python", "omoplate")

# HAND(S) - inmoovGestures\_minimalHand.py
ear.addCommand(u"ouvre les mains", "python", "handsopen")
ear.addCommand(u"ferme les mains", "python", "handsclose")
ear.addCommand(u"ouvre la main droite", "python", "handopen")
ear.addCommand(u"ferme la main droite", "python", "handclose")
ear.addCommand(u"ouvre la main", "python", "handopen")
ear.addCommand(u"ferme la main", "python", "handclose")
ear.addCommand(u"ouvre la main gauche", "python", "lefthandopen")
ear.addCommand(u"ferme la main gauche", "python", "lefthandclose")

# HEAD - inmoovGestures\_minimalHead.py
ear.addCommand(u"attacher la tête", "i01.head", "attach")
ear.addCommand(u"détacher la tête", "i01.head", "detach")
ear.addCommand(u"attacher les yeux", "i01.head.eyeY", "attach")
ear.addCommand(u"détacher les yeux", "i01.head.eyeY", "detach")
ear.addCommand(u"regarde sur ta droite", "python", "lookrightside")
ear.addCommand(u"regarde sur ta gauche", "python", "lookleftside")
ear.addCommand(u"regarde au milieu", "python", "lookinmiddle")


