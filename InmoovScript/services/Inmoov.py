# ##############################################################################
# 								INMOOV SERVICE FILE
# ##############################################################################


# ##############################################################################
# 			i01.moveHand overide
# ##############################################################################


def moveHand(Hand,thumb=-1,index=-1,majeure=-1,ringFinger=-1,pinky=-1,wrist=-1,velocity=-1,autodetach=1,delaydetach=2):
	
		
	#autodetach
	if autodetach==1:
		attachDetachThread(Hand,2)
	
	if thumb>-1:
		Hand.thumb.setVelocity(velocity)
		Hand.thumb.moveTo(thumb)
	if index>-1:
		Hand.index.setVelocity(velocity)
		Hand.index.moveTo(index)
	if majeure>-1:
		Hand.majeure.setVelocity(velocity)
		Hand.majeure.moveTo(majeure)
	if ringFinger>-1:
		Hand.ringFinger.setVelocity(velocity)
		Hand.ringFinger.moveTo(ringFinger)
	if pinky>-1:
		Hand.pinky.setVelocity(velocity)
		Hand.pinky.moveTo(pinky)
	if wrist>-1:
		Hand.wrist.setVelocity(velocity)
		Hand.wrist.moveTo(wrist)
		
#we detach servo is a separated thread because the sleep
def attachDetachThread(element,delayToDetach):
	processThread = threading.Thread(target=delayDetach, args=(element,delayToDetach,))
	processThread.start()
	
def delayDetach(element,delayToDetach):
	element.attach()
	sleep(delayToDetach)
	element.detach()
	#print "detached"
	
