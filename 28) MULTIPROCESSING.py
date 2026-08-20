import time
import  multiprocessing


def cal_square(num):
    for n in num:
        time.sleep(5)
        print("square"+ str(n*n))


def cal_cube(num):
    for n in num:
        time.sleep(5)
        print("cube"+ str(n*n*n))


if __name__=="__main__":
    arr=[2,3,8,9]
    p1=multiprocessing.Process(target=cal_square,args=(arr,))
    p2=multiprocessing.Process(target=cal_cube,args=(arr,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("done")


# second type
import time
import  multiprocessing

square_result=[]
def cal_square(arr):
    global square_result

def cal_square(num):
    for n in num:

        print("square"+ str(n*n))
        square_result.append(n*n)
    print("within a process result" + str(square_result))

if __name__=="__main__":
    arr=[2,3,8,9]
    p1=multiprocessing.Process(target=cal_square,args=(arr,))
    p1.start()
    p1.join()

    print("done")