class human:
    def __init__(self,name,occupation):
        self.name=name
        self.occupation=occupation

    def do_work(self):
        if self.occupation=="tennis player":
            print(self.name,"plays tennis")
        elif self.occupation=="actor":
            print(self.name,"shooting a flim")
    def speak(self):
        print(self.name,"how are u")
a=input("name")
b=input("occupation")
c=human(a,b)

c.do_work()
c.speak()
