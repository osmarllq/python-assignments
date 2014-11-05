
data = []

while True:
 num = raw_input('Enter a number:')
 
 if num == 'done':
   break

 try:
   num = float(num)
 except:
   print 'Invalid input'
   continue

 data.append(num)

largest = max(data)
smallest = min(data)

  
print 'Maximum:', largest
print 'Minimum:', smallest
