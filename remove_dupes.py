def remove_duplicates(n):
  dupes = []
  for a in n:
    if a not in dupes:
      dupes.append(a)
  return dupes


print remove_duplicates(["this", "This", "this", "that"])
