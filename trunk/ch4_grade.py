def computegrade(grade):
 try:
  score = float(grade)
  if score > 1.0 or score < 0.0:
    return 'Score out of range'
  elif score >= 0.9:
    return 'A'
  elif score >= 0.8:
    return 'B'
  elif score >= 0.7:
    return 'C'
  elif score >= 0.6:
    return 'D'
  else:
    return 'F'
 except:
  print "Please enter a number between 0 and 1"