def PlayWithWords(word):
	#FindImage(word)
	talkBlocking(word)
	for i in word.decode( "utf8" ):
		if i.isalpha():
			#print "SAY "+i
			TimeNoSpeak="OFF"
			folderLetterPic=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+"\\alphabet\\"
			print folderLetterPic+i+".jpg"
			try:
				r=ImageDisplay.displayFullScreen(folderLetterPic+i+".jpg")
			except:
				pass
			talk(i)
			sleep(2)
	#FindImage(word)
	sleep(1)
	ImageDisplay.exitFS()
	ImageDisplay.closeAll()