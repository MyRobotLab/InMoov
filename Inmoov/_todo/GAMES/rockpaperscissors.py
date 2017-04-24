# ##############################################################################
#						*** play rock paper scissors ***
#		      Version : 1.1
#	TODO : NEXT APPS NEED CHATBOT IT IS BETTER WITH TOPIC TAG
# ##############################################################################

# This inmoovAPPS need :
inmoovNeeds=[isRightArmActivated,isRightHandActivated,isHeadActivated,EarInterpretEngine=="ear.AddCommand"]

def play_rockpaperscissors():

	if CheckIfRobotCanLaunchAPPS(inmoovNeeds):
		# APPS START

		

		# apps verbal commands
		ear.addCommand("play", "python", "rockpaperscissors2")
		ear.addCommand("ready", "python", "ready")
		ear.addCommand("rock", "python", "rock")
		ear.addCommand("paper", "python", "paper")
		ear.addCommand("scissors", "python", "scissors")

		# play rock paper scissors
		global inmoov
		global human
		inmoov = 0
		human = 0
		

		fullspeed()
		talkBlocking("lets play first to 3 points win")
		sleep(4)
		rockpaperscissors2()
			
		def rockpaperscissors2():
			x = (random.randint(1, 3))
			global inmoov
			global human
			if x == 1:
				ready()
				sleep(2)
				rock()
				sleep(2)
				data = msg_i01_ear_recognized.data[0]  
				if (data == "i have rock"):
					x = (random.randint(1, 3))
					if x == 1:
						talkBlocking("zero zero")
					if x == 2:
						talkBlocking("no no")
					if x == 3:
						talkBlocking("no points")
					sleep(1)
				if (data == "i have paper"):
					x = (random.randint(1, 3))
					if x == 1:
						talkBlocking("paper beats rock")
					if x == 2:
						talkBlocking("your point")
					if x == 3:
						talkBlocking("you got this one")
					human += 1
					sleep(1)
				if (data == "i have scissors"):
					x = (random.randint(1, 3))
					if x == 1:
						talkBlocking("1 point for me")
					if x == 2:
						talkBlocking("going fine")
					if x == 3:
						talkBlocking("rock beats scissors")
					inmoov += 1
					sleep(1)
			if x == 2:
				ready()
				sleep(2)
				paper()
				sleep(2)
				data = msg_i01_ear_recognized.data[0]  
				if (data == "i have rock"):
					x = (random.randint(1, 3))
					if x == 1:
						talkBlocking("1 point")
					if x == 2:
						talkBlocking("paper beats rock")
					if x == 3:
						talkBlocking("my point")
					inmoov += 1
					sleep(1)
				if (data == "i have paper"):
					x = (random.randint(1, 3))
					if x == 1:
						talkBlocking("no points")
					if x == 2:
						talkBlocking("ok lets try again")
						sleep(2)
					if x == 3:
						talkBlocking("again")
					sleep(1)
				if (data == "i have scissors"):
					x = (random.randint(1, 3))
					if x == 1:
						talkBlocking("oh no you get 1 point")
					if x == 2:
						talkBlocking("this is not good for me")
					if x == 3:
						talkBlocking("your point")
					human += 1
					sleep(1)
			if x == 3:
				ready()
				sleep(2)
				scissors()
				sleep(2)
				data = msg_i01_ear_recognized.data[0]  
				if (data == "i have rock"):
					x = (random.randint(1, 3))
					if x == 1:
						talkBlocking("oh no")
					if x == 2:
						talkBlocking("rock beats scissors")
					if x == 3:
						talkBlocking("i feel generous today")
					human += 1
					sleep(1)
				if (data == "i have paper"):
					x = (random.randint(1, 3))
					if x == 1:
						talkBlocking("i've got you")
					if x == 2:
						talkBlocking("my point")
					if x == 3:
						talkBlocking("good")
					inmoov += 1
					sleep(1)
				if (data == "i have scissors"):
					x = (random.randint(1, 3))
					if x == 1:
						talkBlocking("no no")
					if x == 2:
						talkBlocking("zero zero")
					if x == 3:
						talkBlocking("no points")
					sleep(1)
			if inmoov == 3:
				stoprockpaperscissors()
				sleep(1)
			elif human == 3:                       # changed from if to  elif
				stoprockpaperscissors()
				sleep(1)
			elif inmoov <= 2:                      # changed from if to  elif
				rockpaperscissors2()
			elif human <= 2:                       # changed from if to  elif
				rockpaperscissors2()
		  
		def stoprockpaperscissors():
			rest()
			sleep(5)
			global inmoov
			global human
			if inmoov < human:
				talkBlocking("congratulations you won with" + str(human - inmoov) + "points")
				sleep(3)
				talkBlocking(str(human) + "points to you and" + str(inmoov) + "points to me")
			elif inmoov > human:                                                                                                         # changed from if to  elif
				talkBlocking("yes yes i won with" + str(inmoov - human) + "points")
				sleep(3)
				talkBlocking("i've got " + str(inmoov) + "points and you got" + str(human) + "points")
			elif inmoov == human:                                                                                                          # changed from if to  elif
				talkBlocking("none of us won we both got" + str(inmoov) + "points")
			
			inmoov = 0
			human = 0
			
			talkBlocking("that was fun")
			sleep(2)
			talkBlocking("do you want to play again")
			sleep(10)
			data = msg_i01_ear_recognized.data[0]  
			if (data == "yes let's play again"):
				rockpaperscissors2()
			elif (data == "yes"):                                                                              # changed from if to  elif
				rockpaperscissors2()
			elif (data == "no thanks"):                                                                  # changed from if to  elif
				talkBlocking("maybe some other time")
				sleep(4)
				power_down()
			elif (data == "no thank you"):                                                           # changed from if to  elif
				talkBlocking("maybe some other time")
				sleep(4)
				power_down()
			

		def ready():
			talkBlocking("ready")
			talkBlocking("go")
			i01.moveHead(90,90)
			i01.moveArm("left",65,90,75,10)
			i01.moveArm("right",20,80,25,20)
			i01.moveHand("left",130,180,180,180,180,90)
			i01.moveHand("right",50,90,90,90,100,90)
			
			

		def rock():
			fullspeed()
			i01.moveHead(90,90)
			i01.moveArm("left",70,90,80,10)
			i01.moveArm("right",20,80,20,20)
			i01.moveHand("left",130,180,180,180,180,90)
			i01.moveHand("right",50,90,90,90,100,90)
			sleep(.5)
			i01.setHeadSpeed(.8,.8)
			i01.moveHead(60,107)
			i01.moveArm("left",49,90,75,10)
			i01.moveArm("right",20,80,20,20)
			i01.moveHand("left",130,180,180,180,180,90)
			i01.moveHand("right",50,90,90,90,100,90)
			
			sleep(.5)
			i01.moveArm("left",80,90,85,10)
			i01.moveArm("right",20,80,20,20)
			i01.moveHand("left",130,180,180,180,180,90)
			i01.moveHand("right",50,90,90,90,100,90)
			sleep(.5)
			i01.setHeadSpeed(.8,.8)
			i01.moveHead(60,107)
			i01.moveArm("left",49,90,75,10)
			i01.moveArm("right",20,80,20,20)
			i01.moveHand("left",130,180,180,180,180,90)
			i01.moveHand("right",50,90,90,90,100,90)
			
			sleep(.5)
			i01.moveArm("left",90,90,90,10)
			i01.moveArm("right",20,85,10,20)
			i01.moveHand("left",130,180,180,180,180,90)
			i01.moveHand("right",50,90,90,90,100,90)
			sleep(.5)
			i01.setHeadSpeed(.8,.8)
			i01.moveHead(60,107)
			i01.moveArm("left",45,90,75,10)
			i01.moveArm("right",20,80,20,20)
			i01.moveHand("left",130,180,180,180,180,80)
			i01.moveHand("right",50,90,90,90,100,90)
			sleep(.3)
			x = (random.randint(1, 2))
			if x == 1:
				talkBlockingBlocking("i have rock what do you have")
			if x == 2:
				talkBlockingBlocking("what do you have")

		def paper():
			fullspeed()
			i01.moveHead(90,90)
			i01.moveArm("left",70,90,80,10)
			i01.moveArm("right",20,80,20,20)
			i01.moveHand("left",130,180,180,180,180,90)
			i01.moveHand("right",50,90,90,90,100,90)
			sleep(.5)
			i01.setHeadSpeed(.8,.8)
			i01.moveHead(60,107)
			i01.moveArm("left",49,90,75,10)
			i01.moveArm("right",20,80,20,20)
			i01.moveHand("left",130,180,180,180,180,90)
			i01.moveHand("right",50,90,90,90,100,90)
			
			sleep(.5)
			i01.moveArm("left",80,90,85,10)
			i01.moveArm("right",20,80,20,20)
			i01.moveHand("left",130,180,180,180,180,90)
			i01.moveHand("right",50,90,90,90,100,90)
			sleep(.5)
			i01.setHeadSpeed(.8,.8)
			i01.moveHead(60,107)
			i01.moveArm("left",49,90,75,10)
			i01.moveArm("right",20,80,20,20)
			i01.moveHand("left",130,180,180,180,180,90)
			i01.moveHand("right",50,90,90,90,100,90)
			
			sleep(.5)
			i01.moveArm("left",90,90,90,10)
			i01.moveArm("right",20,85,10,20)
			i01.moveHand("left",130,180,180,180,180,90)
			i01.moveHand("right",50,90,90,90,100,90)
			sleep(.5)
			i01.setHeadSpeed(.8,.8)
			i01.moveHead(90,90)
			i01.moveArm("left",49,90,75,10)
			i01.moveArm("right",20,80,20,20)
			i01.moveHand("left",0,0,0,0,0,165)
			i01.moveHand("right",50,90,90,90,100,90)
			sleep(.3)
			x = (random.randint(1, 2))
			if x == 1:
				talkBlockingBlocking("i have paper what do you have")
			if x == 2:
				talkBlockingBlocking("what do you have")

		def scissors():
			fullspeed()
			i01.moveHead(90,90)
			i01.moveArm("left",70,90,80,10)
			i01.moveArm("right",20,80,20,20)
			i01.moveHand("left",130,180,180,180,180,90)
			i01.moveHand("right",50,90,90,90,100,90)
			sleep(.5)
			i01.setHeadSpeed(.8,.8)
			i01.moveHead(60,107)
			i01.moveArm("left",49,90,75,10)
			i01.moveArm("right",20,80,20,20)
			i01.moveHand("left",130,180,180,180,180,90)
			i01.moveHand("right",50,90,90,90,100,90)
			
			sleep(.5)
			i01.moveArm("left",80,90,85,10)
			i01.moveArm("right",20,80,20,20)
			i01.moveHand("left",130,180,180,180,180,90)
			i01.moveHand("right",50,90,90,90,100,90)
			sleep(.5)
			i01.setHeadSpeed(.8,.8)
			i01.moveHead(60,107)
			i01.moveArm("left",49,90,75,10)
			i01.moveArm("right",20,80,20,20)
			i01.moveHand("left",130,180,180,180,180,90)
			i01.moveHand("right",50,90,90,90,100,90)
			
			sleep(.5)
			i01.moveArm("left",90,90,90,10)
			i01.moveArm("right",20,85,10,20)
			i01.moveHand("left",130,180,180,180,180,90)
			i01.moveHand("right",50,90,90,90,100,90)
			sleep(.5)
			i01.moveHead(90,90)
			i01.moveArm("left",49,90,75,10)
			i01.moveArm("right",20,80,20,20)
			i01.moveHand("left",50,0,0,180,180,90)
			i01.moveHand("right",50,90,90,90,100,90)
			sleep(.3)
			x = (random.randint(1, 2))
			if x == 1:
				talkBlockingBlocking("i have scissors what do you have")
			if x == 2:
				talkBlockingBlocking("what do you have")
	else:
		talkBlocking(lang_CannotLaunchAPPS)