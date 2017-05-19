# -- coding: utf-8 --
# ##############################################################################
#						*** INMOOV MINIMAL SPANISH - Thank a lot RODOLPHO ***
# 			  Those actions are inside inmoovGestures
# ##############################################################################


# GENERAL
ear.addCommand(u"desconectar todo", "python", "disableAll()")
ear.addCommand(u"descansar", "python", "rest")
ear.addCommand(u"lista", "python", "rest")
ear.addCommand(u"primero", "python", "rest")
ear.addCommand(u"probar gestos", "python", "gestureTEST")

# ARM((S) - inmoovGestures\ minimalArm.py
ear.addCommand(u"desconectar brazo izquierdo", "i01.leftArm", "disable")
ear.addCommand(u"levanta tu brazo derecho", "python", "rightbicepsraise")
ear.addCommand(u"baja tu brazo derecho", "python", "rightbicepslower")
ear.addCommand(u"levanta tu brazo izquierdo", "python", "leftbicepsraise")
ear.addCommand(u"baja tu brazo izquierdo", "python", "lefttbicepslower")
ear.addCommand(u"brazos adelante", "python", "armsFront")
ear.addCommand(u"da vinci", "python", "daVinci")
ear.addCommand(u"davinci", "python", "daVinci")
ear.addCommand(u"Omóplato", "python", "omoplate")

# HAND(S) - inmoovGestures\ minimalHand.py
ear.addCommand(u"abre tus manos", "python", "handsopen")
ear.addCommand(u"cierra tus manos", "python", "handsclose")
ear.addCommand(u"abre tu mano derecha", "python", "handopen")
ear.addCommand(u"cierra tu mano derecha", "python", "handclose")
ear.addCommand(u"abre tu mano", "python", "handopen")
ear.addCommand(u"cierra tu mano", "python", "handclose")
ear.addCommand(u"abre tu mano izquierda", "python", "lefthandopen")
ear.addCommand(u"cierra tu mano izquierda", "python", "lefthandclose")

# HEAD - inmoovGestures\ minimalHead.py
ear.addCommand(u"Desconectar la Cabeza", "i01.head", "disable")
ear.addCommand(u"desconectar los ojos", "i01.head.eyeY", "disable")
ear.addCommand(u"Mira a la derecha", "python", "lookrightside")
ear.addCommand(u"Mira a la izquierda", "python", "lookleftside")
ear.addCommand(u"Mira al centro", "python", "lookinmiddle")
#to translate
#ear.addCommand(u"search humans", "python", "trackHumans")
#ear.addCommand(u"quit search", "python", "stopTracking")
#ear.addCommand(u"track", "python", "trackPoint")
#ear.addCommand(u"freeze track", "python", "stopTracking")
#ear.addCommand(u"tilt head to the left", "python", "tiltHeadLeftSide")
#ear.addCommand(u"tilt head to the right", "python","tiltHeadRightSide")

# TORSO - inmoovGestures\minimalTorso.py
ear.addCommand("disconnect torso", "i01.torso", "disable")
ear.addCommand("test your stomach", "python", "teststomach")
