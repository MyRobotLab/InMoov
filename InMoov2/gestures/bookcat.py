
def bookcat():
  sleep(3)
  chatBot.getResponse("SAY " + "Tell me read the book or stop reading")
  #chatBot.getResponse("SAY " + "Скажите мне, прочитайте книгу или перестаньте читать")
  sleep(3)
  
  

def bookcatYes():
  print "book cat yes"
  sleep(2)
  inMoov.mouth.speakBlocking("Tell me. turn the page, when you want me to read the next page, or say. stop reading")
  # #inMoov.mouth.speakBlocking(u"Скажите мне. Повернуть страницу, когда вы хотите, чтобы я прочитал следующую страницу или скажите. Прекратить чтение")
  inMoov.moveHead(20,90,30)
  sleep(2)
  inMoov.moveHead(90,90,90)

def bookcatNo():
  print "book cat no"
  sleep(2)
  inMoov.mouth.speakBlocking("too bad, I like this book")
  # #inMoov.mouth.speakBlocking(u"Слишком плохо, мне нравится эта книга")
  inMoov.moveHead(120,90,30)
  sleep(2)
  inMoov.moveHead(90,90,90)

def turnthepage(): 
  global iReadbookcat
  if iReadbookcat <= 0:
    sleep(3)
    inMoov.mouth.speakBlocking("Cat the cat, who is that?")
	# #inMoov.mouth.speakBlocking(u"Кошка кошка, кто это?")
    iReadbookcat += 1
  elif iReadbookcat == 1:
    sleep(3)
    inMoov.mouth.speakBlocking("It's mouse, the mouse! Hi, mouse the mouse!  Hello there")
	# #inMoov.mouth.speakBlocking(u"Это мышь, мышь! Привет, мышь мышь! Привет")
    iReadbookcat += 1
  elif iReadbookcat == 2:
    sleep(3)
    inMoov.mouth.speakBlocking("Cat the cat, who is that?")
	# #inMoov.mouth.speakBlocking(u"Кошка кошка, кто это?")
    iReadbookcat += 1
  elif iReadbookcat == 3:
    sleep(3)
    inMoov.mouth.speakBlocking("It's duck the duck! Hi, duck the duck! A pleasure, as always")
    # #inMoov.mouth.speakBlocking(u"Это утка утка! Привет, утка утка! Удовольствие, как всегда")
    iReadbookcat += 1
  elif iReadbookcat == 4:
    sleep(3)
    inMoov.mouth.speakBlocking("Cat the cat, who is that?")
	# #inMoov.mouth.speakBlocking(u"Кошка кошка, кто это?")
    iReadbookcat += 1
  elif iReadbookcat == 5:
    sleep(3)
    inMoov.mouth.speakBlocking("It's fish the fish! Hi, fish the fish! Hey dude")
	# #inMoov.mouth.speakBlocking(u"Это рыба рыба! Привет, рыба рыба! Привет чувак")
    iReadbookcat += 1
  elif iReadbookcat == 6:
    sleep(3)
    inMoov.mouth.speakBlocking("Cat the cat likes her friends. Sure do")
	# #inMoov.mouth.speakBlocking(u"Кошка кошка любит своих друзей. Конечно да")
    iReadbookcat += 1
  elif iReadbookcat == 7:
    sleep(3)
    inMoov.mouth.speakBlocking("Cat the cat, who is that?  eep")
	# #inMoov.mouth.speakBlocking(u"Кошка кошка, кто это? Ой")
    iReadbookcat += 1
  elif iReadbookcat == 8:
    sleep(3)
    inMoov.mouth.speakBlocking("I have no idea.  blarggie! blarggie")
	# #inMoov.mouth.speakBlocking(u"Понятия не имею.Бларги! Бларги!")
    iReadbookcat += 1
  elif iReadbookcat == 9:
    sleep(3)
    inMoov.mouth.speakBlocking("Maybe")
	# #inMoov.mouth.speakBlocking(u"Может быть")
    iReadbookcat += 1
  elif iReadbookcat == 10:
    sleep(3)
    inMoov.mouth.speakBlocking("Blarggie! Blarggie!  It's a new friend! Blarggie! Blarggie")
	# #inMoov.mouth.speakBlocking(u"Бларги! Бларги! Это новый друг! Бларги! Бларги!")
    iReadbookcat += 1
  elif iReadbookcat == 11:
    sleep(3)
    inMoov.mouth.speakBlocking("The end")
	# #inMoov.mouth.speakBlocking(u"Конец")
    iReadbookcat += 1
  elif iReadbookcat == 12:
    sleep(3)
    inMoov.mouth.speakBlocking("The end")
	# #inMoov.mouth.speakBlocking(u"Конец")
    iReadbookcat += 1
