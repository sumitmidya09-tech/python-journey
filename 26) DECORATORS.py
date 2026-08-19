import time


def cal_square(num):
    start=time.time()
    result=[]
    for nu in num:
        result.append(nu*nu)
    end=time.time()
    print("cal_square took"+ str((end-start)*1000)+"milliseconds")
    return result
def cal_cube(num):
    start=time.time()
    result=[]
    for nu in num:
        result.append(nu*nu*nu)
    end = time.time()
    print("cal_square took" + str((end - start) * 1000) + "milliseconds")
    return result


array=range(1,100000)
out_square=cal_square(array)
out_cube=cal_cube(array)



#second types


import time

def time_it(func):
    def warpper(*args,**kw):
        start=time.time()
        result = func(*args,**kw)
        end=time.time()
        print(func.__name__+"took"+str((end-start)*1000)+"milliseconds")
        return result
    return warpper



@time_it
def cal_square(num):

    result=[]
    for nu in num:
        result.append(nu*nu)
    return result

@time_it
def cal_cube(num):

    result=[]
    for nu in num:
        result.append(nu*nu*nu)
    return result


array=range(1,100000)
out_square=cal_square(array)
out_cube=cal_cube(array)