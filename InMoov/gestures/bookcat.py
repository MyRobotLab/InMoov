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
  global helvar
  if helvar <= 0:
    sleep(3)
    i01.mouth.speakBlocking("Cat the cat, who is that?")
    helvar += 1
  elif helvar == 1:
    sleep(3)
    i01.mouth.speakBlocking("It's mouse, the mouse! Hi, mouse the mouse!  Hello there")
    helvar += 1
  elif helvar == 2:
    sleep(3)
    i01.mouth.speakBlocking("Cat the cat, who is that?")
    helvar += 1
  elif helvar == 3:
    sleep(3)
    i01.mouth.speakBlocking("It's duck the duck! Hi, duck the duck! A pleasure, as always")
    helvar += 1
  elif helvar == 4:
    sleep(3)
    i01.mouth.speakBlocking("Cat the cat, who is that?")
    helvar += 1
  elif helvar == 5:
    sleep(3)
    i01.mouth.speakBlocking("It's fish the fish! Hi, fish the fish! Hey dude")
    helvar += 1
  elif helvar == 6:
    sleep(3)
    i01.mouth.speakBlocking("Cat the cat likes her friends. Sure do")
    helvar += 1
  elif helvar == 7:
    sleep(3)
    i01.mouth.speakBlocking("Cat the cat, who is that?  eep")
    helvar += 1
  elif helvar == 8:
    sleep(3)
    i01.mouth.speakBlocking("I have no idea.  blarggie! blarggie")
    helvar += 1
  elif helvar == 9:
    sleep(3)
    i01.mouth.speakBlocking("Maybe")
    helvar += 1
  elif helvar == 10:
    sleep(3)
    i01.mouth.speakBlocking("Blarggie! Blarggie!  It's a new friend! Blarggie! Blarggie")
    helvar += 1
  elif helvar == 11:
    sleep(3)
    i01.mouth.speakBlocking("The end")
    helvar += 1
