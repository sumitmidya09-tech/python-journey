f=open("c:\\data\\funny.txt","r")
f_out=open("c:\\data\\funny_wc.txt","w")
for line in f:
    t=line.split(" ")
    f_out.write(line+"WORDCOUNT:"+str(len(t)))

f.close()
f_out.close()
