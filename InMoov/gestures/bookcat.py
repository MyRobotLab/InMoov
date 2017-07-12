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
  global bookcat
  if bookcat <= 0:
    sleep(3)
    i01.mouth.speakBlocking("Cat the cat, who is that?")
    bookcat += 1
  elif bookcat == 1:
    sleep(3)
    i01.mouth.speakBlocking("It's mouse, the mouse! Hi, mouse the mouse!  Hello there")
    bookcat += 1
  elif bookcat == 2:
    sleep(3)
    i01.mouth.speakBlocking("Cat the cat, who is that?")
    bookcat += 1
  elif bookcat == 3:
    sleep(3)
    i01.mouth.speakBlocking("It's duck the duck! Hi, duck the duck! A pleasure, as always")
    bookcat += 1
  elif bookcat == 4:
    sleep(3)
    i01.mouth.speakBlocking("Cat the cat, who is that?")
    bookcat += 1
  elif bookcat == 5:
    sleep(3)
    i01.mouth.speakBlocking("It's fish the fish! Hi, fish the fish! Hey dude")
    bookcat += 1
  elif bookcat == 6:
    sleep(3)
    i01.mouth.speakBlocking("Cat the cat likes her friends. Sure do")
    bookcat += 1
  elif bookcat == 7:
    sleep(3)
    i01.mouth.speakBlocking("Cat the cat, who is that?  eep")
    bookcat += 1
  elif bookcat == 8:
    sleep(3)
    i01.mouth.speakBlocking("I have no idea.  blarggie! blarggie")
    bookcat += 1
  elif bookcat == 9:
    sleep(3)
    i01.mouth.speakBlocking("Maybe")
    bookcat += 1
  elif bookcat == 10:
    sleep(3)
    i01.mouth.speakBlocking("Blarggie! Blarggie!  It's a new friend! Blarggie! Blarggie")
    bookcat += 1
  elif bookcat == 11:
    sleep(3)
    i01.mouth.speakBlocking("The end")
    bookcat += 1
  elif bookcat == 12:
    sleep(3)
    i01.mouth.speakBlocking("The end")
    bookcat += 1
