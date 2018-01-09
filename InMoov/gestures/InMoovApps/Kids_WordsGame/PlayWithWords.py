def PlayWithWords(word):
  talkBlocking(word)
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
      talk(i)
      sleep(2)
  sleep(1)
  ImageDisplay.exitFS()
  ImageDisplay.closeAll()