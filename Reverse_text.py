def reverse(text):
  word = [text]
  new_word = ""
  count = len(text) - 1
  for letter in text:
    word.insert(0, letter)
  for a in range(len(word) - 1):
    new_word = new_word +  word[a]
  return new_word

print reverse("This is my text to reverse")
