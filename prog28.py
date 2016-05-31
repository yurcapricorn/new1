with open('dataset.txt', 'r') as input:
    book = []
    for line in input:
        line=line.strip().split()
        book.append(line)

tab=[[i,0,0] for i in range(1,12)]
res=[[i,0] for i in range(1,12)]
ind=0
for i in range(len(book)):
    if int(book[i][0]) in (1,2,3,4,5,6,7,8,9,10,11):
        for j in range(len(tab)):
            if int(res[j][0])==int(book[i][0]):
                tab[j][1]+=int(book[i][2])
                tab[j][2]+=1
for i in range(len(tab)):
    if tab[i][2]==0:
        res[i][1]='-'
    else:
        res[i][1]=float(tab[i][1]/tab[i][2])
for i in range(len(res)):
    print(res[i][0], res[i][1])