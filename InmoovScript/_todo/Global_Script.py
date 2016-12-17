#TODO: explain what this is
#link to main script
##############
# tweaking default settings of jaw
head.jaw.setMinMax(42,101)
head.jaw.map(0,180,42,101)
head.jaw.setRest(42)
##############

# tweaking default settings of eyes
head.eyeY.map(0,180,85,110)
head.eyeY.setMinMax(0,180)
head.eyeY.setRest(90)
head.eyeX.map(0,180,75,120)
head.eyeX.setMinMax(0,180)
head.eyeX.setRest(90)
head.neck.map(0,180,75,128)
head.neck.setMinMax(0,180)
head.neck.setRest(90)
head.rothead.map(0,180,60,130)
head.rothead.setMinMax(0,180)
head.rothead.setRest(90)
##############

# tweaking default torso settings
#torso.topStom.setMaxVelocity(13)
torso.topStom.setMinMax(60,120)
torso.topStom.map(0,180,60,120)
#torso.midStom.setMaxVelocity(13)
torso.midStom.setMinMax(0,180)
torso.midStom.map(0,180,50,130)
#torso.lowStom.setMaxVelocity(13)
#torso.lowStom.setMinMax(0,180)
#torso.lowStom.map(0,180,60,120)
torso.topStom.setRest(90)
torso.midStom.setRest(90)
#torso.lowStom.setRest(90)
##############

# tweaking default settings of left hand
#leftHand.thumb.setMaxVelocity(250)
leftHand.thumb.setMinMax(0,180)
#leftHand.index.setMaxVelocity(250)
leftHand.index.setMinMax(0,180)
#leftHand.majeure.setMaxVelocity(250)
leftHand.majeure.setMinMax(0,180)
#leftHand.ringFinger.setMaxVelocity(250)
leftHand.ringFinger.setMinMax(0,180)
#leftHand.pinky.setMaxVelocity(250)
leftHand.pinky.setMinMax(0,180)
#leftHand.wrist.setMaxVelocity(250)
leftHand.wrist.setMinMax(0,180)
leftHand.thumb.map(0,180,62,150)
leftHand.index.map(0,180,35,135)
leftHand.majeure.map(0,180,35,180)
leftHand.ringFinger.map(0,180,45,150)
leftHand.pinky.map(0,180,50,170)
leftHand.wrist.map(0,180,40,130)
###############

#tweak defaults LeftArm
#leftArm.bicep.setMaxVelocity(26)
leftArm.bicep.setMinMax(5,95)
leftArm.bicep.map(0,180,45,140)
#leftArm.rotate.setMaxVelocity(18)
leftArm.rotate.setMinMax(40,180)
leftArm.rotate.map(40,180,60,142)
#leftArm.shoulder.setMaxVelocity(14)
leftArm.shoulder.setMinMax(0,180)
leftArm.shoulder.map(0,180,42,150)
#leftArm.omoplate.setMaxVelocity(15)
leftArm.omoplate.setMinMax(10,82)
leftArm.omoplate.map(0,180,36,135)
################

# tweaking defaults settings of right hand
#rightHand.thumb.setMaxVelocity(250)
rightHand.thumb.setMinMax(0,180)
#rightHand.index.setMaxVelocity(250)
rightHand.index.setMinMax(0,180)
#rightHand.majeure.setMaxVelocity(250)
rightHand.majeure.setMinMax(0,180)
#rightHand.ringFinger.setMaxVelocity(250)
rightHand.ringFinger.setMinMax(0,180)
#rightHand.pinky.setMaxVelocity(250)
rightHand.pinky.setMinMax(0,180)
#rightHand.wrist.setMaxVelocity(250)
rightHand.wrist.setMinMax(0,180)
rightHand.thumb.map(0,180,64,135)
rightHand.index.map(0,180,42,160)
rightHand.majeure.map(0,180,35,165)
rightHand.ringFinger.map(0,180,40,140)
rightHand.pinky.map(0,180,45,130)
rightHand.wrist.map(0,180,30,135)
#################

# tweak default RightArm
#rightArm.bicep.setMaxVelocity(26)
rightArm.bicep.setMinMax(5,95)
rightArm.bicep.map(0,180,45,140)
#rightArm.rotate.setMaxVelocity(18)
rightArm.rotate.setMinMax(40,180)
rightArm.rotate.map(40,180,75,130)
#rightArm.shoulder.setMaxVelocity(14)
rightArm.shoulder.setMinMax(0,180)
rightArm.shoulder.map(0,180,42,150)
#rightArm.omoplate.setMaxVelocity(15)
rightArm.omoplate.setMinMax(10,82)
rightArm.omoplate.map(0,180,45,135)
#################

#################
#to tweak the default PID values
eyesTracking.pid.setPID("eyeX",12.0,1.0,0.1)
eyesTracking.pid.setPID("eyeY",12.0,1.0,0.1)
headTracking.pid.setPID("rothead",5.0,1.0,0.1)
headTracking.pid.setPID("neck",5.0,1.0,0.1)
#################
