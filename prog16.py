#some changes
#Sample Input:
# a3b4c2e10b1
#Sample Output:
# aaabbbbcceeeeeeeeeeb

with open('input.txt', 'r') as input:
    s1=input.readline().strip()

#s1='a3b4c2e10b1'
s2=''
nr=''
sym=''
for i in range(len(s1)):
	if s1[i] in ('1234567890'):
	    nr+=s1[i]
	    if i==len(s1)-1:
	        s2+=sym*int(nr)
	else:
	    if len(nr)>0:
	        s2+=sym*int(nr)
	        nr=''	       
	    sym=s1[i]
with open('output.txt', 'w') as output:
    output.write(s2)
		
		