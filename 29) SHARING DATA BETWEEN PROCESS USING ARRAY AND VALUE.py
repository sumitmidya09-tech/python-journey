
import  multiprocessing


def cal_square(num,result,v):
    v.value=5.67
    for idx,n in enumerate(num):
        result[idx]=n*n

if __name__=="__main__":
    num=[2,3,8,9]
    result=multiprocessing.Array("i",4)
    v=multiprocessing.Value("d",0.0)
    p1=multiprocessing.Process(target=cal_square,args=(num,result,v))
    p1.start()
    p1.join()
    print(v.value)