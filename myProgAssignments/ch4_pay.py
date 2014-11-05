
def computepay(hours,rate):
 try:
  hours = float(hours)
  rate = float(rate)
  if hours > 40:
   extra = (hours-40) * (rate*1.5)
   pay = 40 * rate
   tpay = extra + pay
  else:
   tpay = hours * rate 
  return tpay
 except:
  print 'Error, please provide numeric input' 
