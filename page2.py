#Use of this page is optional. If you use code here, make sure either import page2 or from page2 import * appear on your main.py page.



def art (guessesremaining):
  if guessesremaining == 6:
    print ("––––|")
    print (" |  |")
    print ("    |")
    print ("    |")
    print ("    |")
    print ("    |")
    print ("–––––––––")

  if guessesremaining == 5:
    print ("––––|")
    print (" |  |")
    print (" O  |")
    print ("    |")
    print ("    |")
    print ("    |")
    print ("–––––––––")

  if guessesremaining == 4:
    print ("––––|")
    print (" |  |")
    print (" O  |")
    print (" |  |")
    print ("    |")
    print ("    |")
    print ("–––––––––")

  if guessesremaining == 3:
    print ("––––|")
    print (" |  |")
    print ("\O  |")
    print (" |  |")
    print ("    |")
    print ("    |")
    print ("–––––––––")

  if guessesremaining == 2:
    print ("––––|")
    print (" |  |")
    print ("\O/ |")
    print (" |  |")
    print ("    |")
    print ("    |")
    print ("–––––––––")

  if guessesremaining == 1:
    print ("––––|")
    print (" |  |")
    print ("\O/ |")
    print (" |  |")
    print ("/   |")
    print ("    |")
    print ("–––––––––")

  if guessesremaining == 0:
    print ("––––|")
    print (" |  |")
    print ("\O/ |")
    print (" |  |")
    print ("/ \ |")
    print ("    |")
    print ("–––––––––")