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