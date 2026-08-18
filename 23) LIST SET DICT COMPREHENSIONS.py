num=[1,2,3,4,5,6,7]
even=[]
for i in num:
    if i%2==0:
        even.append(i)

print(even)

even=[i for i in num if i%2==0]
print(even)


sqr_numb=[i*i for i in num]
print(sqr_numb)


#set

s=set([1,2,3,1,1,5,6])
print(s)
even={i for i in s if i%2==0}
print(even)


#next

cities=["mumbai","hangzhou","paris","shanghai"]
countries=["india","usa","china","france"]
z=zip(cities,countries)
print(z)
for i in z:
    print(i)

d={city:country for city,country in zip(cities,countries)}
print(d)

