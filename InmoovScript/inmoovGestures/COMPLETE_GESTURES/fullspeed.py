def fullspeed():
	#neopixel.setAnimation("Color Wipe", 200, 0, 0, 1)
	#sleep(1)
	#neopixel.setAnimation("Ironman", 0, 0, 255, 1)
	i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
	i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
	i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
	i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
	i01.setHeadSpeed(1.0, 1.0)
	i01.setTorsoSpeed(1.0, 1.0, 1.0)

