with open('dataset.txt', 'r') as input:
    book = []
    for line in input:
        line=line.strip().split(';')
        book.append(line)

stud=''
bal=0
for i in range(len(book)):
    for j in range(1,4):
        bal+=int(book[i][j])
    stud+=str(bal/3)+'\n'
    bal=0

balobsh=0
srobsh=''
for j in range(1,4):
    for i in range(len(book)):
        balobsh+=int(book[i][j])
    srobsh+=str(balobsh/(len(book)))+' '
    balobsh=0

with open('output.txt', 'a') as output:
    output.write(stud)
    output.write(srobsh)