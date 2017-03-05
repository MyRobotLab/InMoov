# ##############################################################################
# 								ARDUINO SERVICE FILE
# ##############################################################################


# ##############################################################################
# ARDUINO RELATED FUNCTIONS
# ##############################################################################


	
	
#function to check arduino & mrlcomm
def CheckArduinos(Card,Port,slave=0):
	#A RX/TX connection don't return 'arduino is connected', only mrlcomm version
	if slave!=0:
		Card.connect(slave,Port)
		sleep(1)
	else:
		Card.connect(Port)
		sleep(1)
		for i in range(0,10):
			if not Card.isConnected():
				Card.disconnect()
				sleep(0.1)
				Card.connect(Port)
				sleep(0.5)
			else:
				break
		
	if ForceArduinoIsConnected:return True
	else:
		if not Card.isConnected() and slave==0:
			errorSpokenFunc('ArduinoNotConnected',Port)
			return False
		if Card.isConnected() or slave!=0:
			print "Mrlcomm version : ",Card.getBoardInfo().version," ( requiered ",MRLCOMM_VERSION," )"
			if Card.getBoardInfo().version!=MRLCOMM_VERSION:errorSpokenFunc('BadMrlcommVersion',Port)
			else:
				print "Arduino ",Port," OK"
				return True

			
#analog pin listener
def publishPinLeft(pins):
	global AudioInputValues
	
	for pin in range(0, len(pins)):
		
		#mouth control listener
		if isHeadActivated:
			if AudioSignalProcessingCalibration:AudioInputValues.append(pins[pin].value)
				
			if AudioSignalProcessing:
				if pins[pin].value>minAudioValue:
					head.jaw.moveTo(pins[pin].value)
				

	
	



    

