import time
import threading



def cal_square(num):
    print("calculater square number")
    for n in num:
        time.sleep(0.2)
        print("square",n*n)


def cal_cube(num):
    print("calculater cube number")
    for n in num:
        time.sleep(0.2)
        print("cube",n*n*n)


arr=[2,3,8,9]
t=time.time()
t1=threading.Thread(target=cal_square,args=(arr,))
t2=threading.Thread(target=cal_cube,args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("done in",time.time()-t)
print("hah i am done with all my work now")
