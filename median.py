def median(n):
  n = sorted(n)
  if len(n) % 2 == 0:
    a = (len(n) / 2) - 1
    b = (len(n) / 2)
    return float((n[a] + n[b]) / 2.0)
  else:
    a = (len(n) / 2)
    return float(n[a])

print median([2, 3, 4, 7, 7, 9])
