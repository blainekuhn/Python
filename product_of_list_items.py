def product(n):
  total = 1
  for item in n:
    total *= item
  if total == 1:
    return (total - 1)
  return total

print product([4, 5, 10])
