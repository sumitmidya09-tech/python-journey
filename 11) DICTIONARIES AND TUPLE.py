#dictionaries
d={"tom":324234234234,"rob":3245983475973498,"joe":34759834759}
print("tom: ",d["tom"])
d["sam"]=38273648623847623
print(d)
del d["sam"]
print(d)
for key in d:
    print("key:",key,"value:",d[key])


for k,v in d.items():
    print("key: ",k,"value: ",v)


a="tom" in d
print(a)
b="sumit" in d
print(b)
d.clear()
print(d)

#tuples

point=(5,6)
a=point[0]
print(a)
b=point[1]
print(b)
# we can not change the value in tuple
#point[0]=50
#error type 