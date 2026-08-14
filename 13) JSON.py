from winreg import OpenKeyEx

book={}
book["tom"] = {
    "name":"tom",
    "address":"1 red street. NY",
    "phone":"98998898"
}
book["bob"] = {
    "name":"bob",
    "address":"1 green street. NY",
    "phone":"232323232"
}
import json
s=json.dumps(book)
print(s)
with open("c://data//book.txt","w") as f:
    f.write(s)


f=open("c://data//book.txt","r")
s=f.read()
print(s)


import json
book=json.loads(s)
print(book)
v=type(book)
print(v)
a=book["bob"]
print(a)
c=book["bob"] ["phone"]
print(c)

for person in book:
    print(book[person])