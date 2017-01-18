def talk(data):
	if data[0:2]=="l ":
		data=data.replace("l ", "l'")
	#data=data.replace(" l ", " l'")
	
        ear.startListening() #fix onclick micro
	
        if data!="":mouth.speak(unicode(data,"utf-8"))