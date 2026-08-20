import  multiprocessing

def cal_square(num,q):

    for n in num:
        q.put(n*n)


if __name__=="__main__":
    num=[2,3,8,9]
    q=multiprocessing.Queue()
    p1=multiprocessing.Process(target=cal_square,args=(num,q))
    p1.start()
    p1.join()


    while q.empty() is False:
        print(q.get())
