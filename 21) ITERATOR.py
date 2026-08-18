a=["hey","bro","you'r","awesome"]
for i in a:
    print(i)


#ITERATORS

itr=iter(a)
print(itr)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))



itr=reversed(a)
print(itr)
print(next(itr))
print(next(itr))
print(next(itr))


#class

class remotecontrol():
    def __init__(self):
        self.channels=["hbo","cnn","abc","espn"]
        self.index=-1
    def __iter__(self):

        return self
    def __next__(self):
        self.index+=1
        if self.index==len(self.channels):
            raise StopIteration
        return self.channels[self.index]
r=remotecontrol()
itr=iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
