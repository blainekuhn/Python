#Censor a word in string - replacing with *** equal to the length of the censored word

def censor(text, word):
  count = 0
  parse = text.split()
 #   while count <= len(parse):
  for w in parse:
  #print w
    if w == word:
      parse[count] = len(word) * "*"
      #parse.remove(w)
    count += 1
  return " ".join(parse)

print censor("This is the text being parsed", "being")
