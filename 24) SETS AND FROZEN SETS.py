basket={"orange","apple","banana","apple","apple"}
ty=type(basket)
print(ty)
print(basket)
a=set()
a.add(1)
a.add(2)
print(a)
a={}
b=type(a)
print(b)
a={"something"}
b=type(a)
print(b)

#next

num=[1,2,3,1,1,2,5,4,7]
unique_numbers=set(num)
print(unique_numbers)
unique_numbers.add(6)
print(unique_numbers)


# frozen mean do not changes


fs=frozenset(num)
print(fs)
#fs.add(6)


#next


x={"a","b","c"}
v="a" in x
print(v)
v="g" in x
print(v)



for i in x:
    print(i)

print(x)

y={"a","f","k"}
print(y)


b=x|y
print(b)
c=x&y
print(c)
d=x-y
print(d)
e=x^y
print(e)
