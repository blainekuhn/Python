#Remove Vowels

def anti_vowel(text):
  vowels = ["a", "e", "i", "o", "u"]
  mylist = []
  newlist = ""
  for a in text:
    mylist += a
  #print "This is my list %s" % mylist
  for s in range(0, len(mylist)):
    if mylist[s].lower() in vowels or mylist[s].upper() in vowels:
      pass
    else:
      newlist = newlist + (mylist[s])
    #print mylist[s]

  return newlist

print anti_vowel("This is my string with vowels removed")


#simple
def non_vowels(text):
    t=""
    for c in text:
        for i in "ieaouIEAOU":
            if c==i:
                c=""
            else:
                c=c
        t=t+c
    return t

print non_vowels("This is my text with vowels removed")
