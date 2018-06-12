import urllib2
def allume():
  print urllib2.urlopen("http://www.google.fr").read()
  print "OK !"

allume()