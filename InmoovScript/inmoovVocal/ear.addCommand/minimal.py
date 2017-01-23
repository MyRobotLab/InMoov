# ##############################################################################
#						*** INMOOV MINIMAL ***
# 			  Those actions are inside inmoovGestures
# ##############################################################################


# GENERAL
ear.addCommand(lang_attach_everything, "i01", "attach")
ear.addCommand(lang_disconnect_everything, "i01", "detach")
ear.addCommand(lang_rest, "python", "rest")
ear.addCommand(lang_list, "python", "rest")
ear.addCommand(lang_first, "python", "rest")

# ARM((S) - inmoovGestures\_minimalArm.py
ear.addCommand(lang_attach_left_arm, "i01.leftArm", "attach") #to remove soon
ear.addCommand(lang_disconnect_left_arm, "i01.leftArm", "detach") #to remove soon
ear.addCommand(lang_raise_your_right_bicep, "python", "rightbicepsraise")
ear.addCommand(lang_lower_your_right_bicep, "python", "rightbicepslower")
ear.addCommand(lang_raise_your_left_bicep, "python", "leftbicepsraise")
ear.addCommand(lang_lower_your_left_bicep, "python", "lefttbicepslower")
ear.addCommand(lang_arms_front, i01.getName(), "armsFront")
ear.addCommand(lang_da_vinci, i01.getName(), "daVinci")
ear.addCommand(lang_omoplate, "python", "omoplate")

# HAND(S) - inmoovGestures\_minimalHand.py
ear.addCommand(lang_open_your_hands, "python", "handsopen")
ear.addCommand(lang_close_your_hands, "python", "handsclose")
ear.addCommand(lang_open_your_right_hand, "python", "handopen")
ear.addCommand(lang_close_your_right_hand, "python", "handclose")
ear.addCommand(lang_open_your_hand, "python", "handopen")
ear.addCommand(lang_close_your_hand, "python", "handclose")
ear.addCommand(lang_open_your_left_hand, "python", "lefthandopen")
ear.addCommand(lang_close_your_left_hand, "python", "lefthandclose")

# HEAD - inmoovGestures\_minimalHead.py
ear.addCommand(lang_attach_head, "i01.head", "attach")
ear.addCommand(lang_disconnect_head, "i01.head", "detach")
ear.addCommand(lang_attach_eyes, "i01.head.eyeY", "attach")
ear.addCommand(lang_disconnect_eyes, "i01.head.eyeY", "detach")
ear.addCommand(lang_look_on_your_right_side, "python", "lookrightside")
ear.addCommand(lang_look_on_your_left_side, "python", "lookleftside")
ear.addCommand(lang_look_in_the_middle, "python", "lookinmiddle")


