grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
  result = 0
  for a in scores:
    result += a
  return result

def grades_average(grades_input):
  average = grades_sum(grades_input) / float(len(grades_input))
  return average
  
def grades_variance(scores):
  variance = 0
  for score in scores:
    variance += (grades_average(scores) - score) ** 2
    variance = variance / len(scores)
  return variance
  
  
  
print grades_variance(grades)
