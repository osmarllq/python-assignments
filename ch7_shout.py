file = raw_input('Enter a file name:')

try:
 fhand = open(file)
except:
 print 'File cannot be opened:', file
 exit()

for line in fhand:
 print line.upper()

#fhand=open('D:\Documentos\Datos\IPM\BD Sisben Enero\Sisben_Enero.csv')

#count = 0
#for line in fhand:
# count = count + 1

#print 'Line Count:', count
