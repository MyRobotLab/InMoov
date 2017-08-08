def bookcat():
  sleep(3)
  chatBot.getResponse("SAY " + "Tell me read the book or stop reading")
  sleep(3)

def bookcatYes():
  print "book cat yes"
  sleep(2)
  i01.mouth.speakBlocking("Tell me. turn the page, when you want me to read the next page, or say. stop reading")
  i01.moveHead(20,90,30)
  sleep(2)
  i01.moveHead(90,90,90)

def bookcatNo():
  print "book cat no"
  sleep(2)
  i01.mouth.speakBlocking("too bad, I like this book")
  i01.moveHead(120,90,30)
  sleep(2)
  i01.moveHead(90,90,90)

def turnthepage(): 
  global iReadbookcat
  if iReadbookcat <= 0:
    sleep(3)
    i01.mouth.speakBlocking("Cat the cat, who is that?")
    iReadbookcat += 1
  elif iReadbookcat == 1:
    sleep(3)
    i01.mouth.speakBlocking("It's mouse, the mouse! Hi, mouse the mouse!  Hello there")
    iReadbookcat += 1
  elif iReadbookcat == 2:
    sleep(3)
    i01.mouth.speakBlocking("Cat the cat, who is that?")
    iReadbookcat += 1
  elif iReadbookcat == 3:
    sleep(3)
    i01.mouth.speakBlocking("It's duck the duck! Hi, duck the duck! A pleasure, as always")
    iReadbookcat += 1
  elif iReadbookcat == 4:
    sleep(3)
    i01.mouth.speakBlocking("Cat the cat, who is that?")
    iReadbookcat += 1
  elif iReadbookcat == 5:
    sleep(3)
    i01.mouth.speakBlocking("It's fish the fish! Hi, fish the fish! Hey dude")
    iReadbookcat += 1
  elif iReadbookcat == 6:
    sleep(3)
    i01.mouth.speakBlocking("Cat the cat likes her friends. Sure do")
    iReadbookcat += 1
  elif iReadbookcat == 7:
    sleep(3)
    i01.mouth.speakBlocking("Cat the cat, who is that?  eep")
    iReadbookcat += 1
  elif iReadbookcat == 8:
    sleep(3)
    i01.mouth.speakBlocking("I have no idea.  blarggie! blarggie")
    iReadbookcat += 1
  elif iReadbookcat == 9:
    sleep(3)
    i01.mouth.speakBlocking("Maybe")
    iReadbookcat += 1
  elif iReadbookcat == 10:
    sleep(3)
    i01.mouth.speakBlocking("Blarggie! Blarggie!  It's a new friend! Blarggie! Blarggie")
    iReadbookcat += 1
  elif iReadbookcat == 11:
    sleep(3)
    i01.mouth.speakBlocking("The end")
    iReadbookcat += 1
  elif iReadbookcat == 12:
    sleep(3)
    i01.mouth.speakBlocking("The end")
    iReadbookcat += 1
