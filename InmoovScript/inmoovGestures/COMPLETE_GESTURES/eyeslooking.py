def eyeslooking(data):
  for y in range(0, 5):
    if (data == "can i have your attention"):
      i01.mouth.speak("ok you have my attention")
      stopit()
    if (data == "inmoov"):
      stopit()
    x = (random.randint(1, 6))
    if x == 1:
      i01.head.eyeX.moveTo(80)
    if x == 2:
      i01.head.eyeY.moveTo(80)
    if x == 3:
      eyesdown()
    if x == 4:
      eyesupp()
    if x == 5:
      eyesleft()
    if x == 6:
      eyesright()
    sleep(0.5)
  eyesfront()

