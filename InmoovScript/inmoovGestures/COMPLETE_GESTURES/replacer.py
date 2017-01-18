#We intercept what the robot is listen to change some values
#here we replace ' by space because AIML doesn't like '
def replacer(data):
    data = data.replace("'", " ")
    data = data.replace("-", " ")
    data = data.replace(chr(232),"E")#è
    data = data.replace(chr(233),"E")#é
    data = data.replace(chr(234),"E")#ê
    data = data.replace(chr(235),"E")#ë
    data = data.replace(chr(249),"U")#ù
    data = data.replace(chr(251),"U")#û
    data = data.replace(chr(224),"A")#à
    data = data.replace(chr(226),"A")#â
    data = data.replace(chr(212),"O")#ô
    data = data.replace(chr(239),"I")#ï
    print data
    #print ord(data[0])
    inmoovFrench.getResponse(data)

    #German replacer
    #data = data.replace(chr(228),"AE")
    #data = data.replace(chr(246),"OE")
    #data = data.replace(chr(252),"UE")