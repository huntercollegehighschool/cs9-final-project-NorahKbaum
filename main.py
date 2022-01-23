"""
Name(s): Norah Kerschbaum and Grisha London
Name of Project: Hangman.py
"""

#Write the main part of your program here. Use of the other pages is optional.

#import page4  # uncomment if you're using page4


tryagain="y"
list_c = []
from page1 import words
while tryagain!="n":
  from page2 import art
  import random
  import os
  os.system('clear')
  guessesremaining=6
  art(guessesremaining)
  word=words[random.randint(0,(len(words)-1))]
  list_a = list(word)
  list_b = []
  list_c.append(word)
  words.remove(word)
  for i in range(0,len(list_a)):
    list_b.append("_")
  x = " ".join(list_b)
  print("The word or phrase:", x)
  list_guess=[]
  list_guessb=[]
  while guessesremaining>0:
    list_guessc=[" "]
    guessletter=input("What character would you like to guess? If you want to guess a whole word type 'word': ")
    guessletter=guessletter.lower()
    if guessletter == "word":
      guessword=input("What word would you like to guess? ")
      if list(guessword)==list_a:
        list_b=list_a
        from page3 import dancingcat
        dancingcat(600)
        break
      else:
          os.system('clear')     
          print("YOU HAVE FAILED THE CAT. THEY ARE DISAPPOINTED IN YOU AND IN THE WORLD AT LARGE. The word was:","".join(list_a))
          from page3 import vaguelydispleasedcat
          vaguelydispleasedcat(1)
          list_b=list(guessword)
          break
    if guessletter == "":
      guessletter=input("You cannot guess this character, please guess another: ")
    while (guessletter) in list_guess:
      guessletter=input("You have already guessed that character, please guess another: ")
    list_guess.append(guessletter)
    list_guessb.append(guessletter)
    for i in range (0, len(list_a)):
      if guessletter==list_a[i]:
       list_b[i]=guessletter
      if (guessletter) in list_a and (guessletter) in list_guessb:
        list_guessb.remove(guessletter)
    guessesremaining=6-len(list_guessb)    
    os.system('clear')

    art(guessesremaining)
    x=','.join(list_guess)
    print ("Guessed characters:", x)
    x = " ".join(list_b)
    print (x)
    if list_b==list_a:
      from page3 import dancingcat
      dancingcat(600)
      break
  if list_b != list_a:
    os.system('clear')
    print("YOU HAVE FAILED THE CAT. THEY ARE DISAPPOINTED IN YOU AND IN THE WORLD AT LARGE. The word was:","".join(list_a))
    from page3 import vaguelydispleasedcat
    vaguelydispleasedcat(1)
  tryagain=input("Would you like to try again? y/n: ")
  while tryagain !="y" and tryagain!="n":
    tryagain=input("Would you like to try again? y/n: ")
  os.system('clear')
  if len(list_c) > 5:
    words.append(list_c[0])
    list_c.remove(list_c[0])
os.system('clear')
print("Have a good day!")