import requests

link = open('C:\PyProg\dataset.txt').read().strip()

r=requests.get(url=link)

print(len(r.text.splitlines()))