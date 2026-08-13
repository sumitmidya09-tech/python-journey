item1="bread"
item2="pasta"
item3="fruits"
items=["bread","pasta","fruits","veggies"]
print(items)
a=items[0]
print(a)
b=items[2]
print(b)
c=items[0:2]
print(c)
d=items[-1]
print(d)

e=items.append('butter')
print(items)
items=["bread","pasta","fruits","veggies"]
f=items.insert(1,'butter')
print(items)



food=["bread","pasta","fruits"]
bathroom=["shampoo",'soap']
items=food+bathroom
print(items)
a=len(items)
print(a)
b='bread' in items
print(b)
c='veggies' in items
print(c)
