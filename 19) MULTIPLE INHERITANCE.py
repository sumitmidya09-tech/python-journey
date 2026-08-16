class father():
    def gardening(selfself):
        print("i enjoy gardening")

class mother():
    def cooking(selfself):
        print("i love cooking")

class child(father,mother):
    def sport(selfself):
        print("i enjoy sporting")

c=child()
c.gardening()
c.cooking()
c.sport()

class father():
    def skill(selfself):
        print("gardening,programming")

class mother():
    def skill(selfself):
        print("art, cooking")

class child(father,mother):
    def skill(selfself):
        father.skill(selfself)
        mother.skill(selfself)
        print("sporting")


c=child()
c.skill()