def PlayWithWords(word):
  i01.speakBlocking(word)
  i01.stopVinMoov()   #vinmoov+imagedisplay=bug
  for i in word.decode( "utf8" ):
    if i.isalpha():
      alphabet="alphabet"
      if Language.lower()=="ru":alphabet="alphabet_ru"
      folderLetterPic=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+"\\"+alphabet+"\\"
      try:
        r=ImageDisplay.displayFullScreen(folderLetterPic+i+".jpg")
      except:
        pass
      i01.speak(i)
      sleep(2)
  sleep(1)
  ImageDisplay.exitFS()
  ImageDisplay.closeAll()