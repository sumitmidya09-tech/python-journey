tom_exp_list=[21001,2342,5645]
joe_exp_list=[3453,43543,6756]

total=0

for item in tom_exp_list:
    total=total+item
print("tom total expenses: ",total)

total=0

for item in joe_exp_list:
    total=total+item
print("joe total expenses: ",total)

#smart program to write

def calculate_total(exp):
    total=0
    for item in exp:
        total=total+item
    return total


tom_exp_list=[21001,2342,5645]
joe_exp_list=[3453,43543,6756]

tom_total=calculate_total(tom_exp_list)
joe_total=calculate_total(joe_exp_list)

print("tom total expenses: ",tom_total)
print("joe total expenses: ",joe_total)

#second program

def sum(a,b):
    total=a+b
    return total

n=sum(5,9)
print("total:",n)
