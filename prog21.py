'''import requests

r=requests.get('http://example.com')

print(r.text)



url='http://example.com'

par={'key1': 'value1', 'key2': 'value2'}

r=requests.get(url, params=par)

print(r.url)



url='http://httpbin.org/cookies'

cookies={'cookies_are': 'working'}

r=requests.get(url, cookies=cookies)

print(r.text)



print(r.cookies['example_cookie_name'])



print(requests.get(<url>).text)'''



import requests


with open ('C:\PyProg\dataset.txt') as inf:

    url=inf.readline().strip()


with open('output.txt', 'w') as output:
    output.write('')
i=1
a=''
while a[0:2]!='We':

    r=requests.get(url)
    url='https://stepic.org/media/attachments/course67/3.6.3/'+r.text
    print(i)
    i+=1
    a=r.text
    print(r.text)
    print(a[0:2])
with open('output.txt', 'a') as output:
    output.write(a)

'''import requests
link = open('C:\PyProg\dataset.txt').read().strip()
r=requests.get(url=link)
print(len(r.text.splitlines()))'''