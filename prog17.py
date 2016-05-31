# Sample Input:
# abc a bCd bC AbC BC BCD bcd ABC
# Sample Output:
# abc 3

with open('dataset.txt', 'r') as input:
    s1=input.read().strip().lower()

#s1=('abc a bCd bC AbC BC BCD bcd ABC')
s2=[i for i in s1.split()]
res=''
count=1
d={}
max='z'
for i in range(len(s2)):
	if s2[i] not in d:
	    d[s2[i]]=1
	    
	else:
	    d[s2[i]]+=1
	    if d[s2[i]]>count:
	        count+=1

for key, value in d.items():
    if value==count:
        if key<max:
            max=key

res+=max+' '
res+=str(count)

for key, value in d.items():
    print(key, value)	

with open('output.txt', 'w') as output:
    output.write(res)