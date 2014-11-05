#Parsing
str = 'X-DSPAM-Confidence:  0.8475'

#Parse the previous variable and get the slice after the colon

pos = str.find(':')
float(str[pos+1:])


#Get the host:
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

atpos = data.find('@')
print atpos

sppos = data.find(' ',atpos)
print sppos

host = data[atpos+1:sppos]
print host

