hours=raw_input('Enter hours:')
rate=raw_input('Enter rate:')
pay=round(float(hours)*float(rate),2)
out='Pay:'
print out + str(pay)