class accident(Exception):
    def __init__(self,msg):
        self.msg = msg
    def print_exception(self):
        print("user defined exception: ",self.msg)




try:
    raise accident("crash between two car")
except accident as e:
    e.print_exception()

#second



class accident(Exception):
    def __init__(self,msg):
        self.msg = msg
    def handle(self):
        print("accident occured. take detour")






try:
    raise accident("crash between two car")
except accident as e:
    e.handle()


#third


def process_file():
    try:
        f=open("c:\\code\\data.txt")
        x=1/0
    except FileNotFoundError as e:
        print("file not found")
    finally:
        print(" cleaning up files")
        f.close()


process_file()