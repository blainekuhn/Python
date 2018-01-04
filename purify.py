def purify(n):
  even = []
  count = 0
  for i in n:
    if (i % 2) == 0:
      even.append(i)
    count += 1
  return even

print purify([1,2,3,4,5,6,7,8])
