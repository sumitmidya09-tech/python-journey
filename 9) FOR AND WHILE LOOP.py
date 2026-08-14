exp=[1233,6456,2343,23556,2332]
total=exp[0]+exp[1]+exp[2]+exp[3]+exp[4]
print(total)

#long statement

#sort way to write
exp=[1233,6456,2343,23556,2332]
total=0
for item in exp:
    total+=item
print(total)


#second program

for i in range (1,11):
    print(i*i)


#third program

exp=[1233,6456,2343,23556,2332]
total=0
for i in range(len(exp)):
    print("month: ",(i+1),'expense: ',exp[i])
    total+=exp[i]
print("total expsnse is: ",total)



#fourth program


key_loction="chair"
locations=['garage','living room','chair','closet']
for i in locations:
    if i==key_loction:
        print("key is found in: ",i)
        break
    else:
        print("key is not found in: ",i)



#fifth program


for i in range(1,6):
    if i%2==0:
        continue
    print(i*i)




#sixth program


i=1
while i<=5:
    print(i)
    i=i+1