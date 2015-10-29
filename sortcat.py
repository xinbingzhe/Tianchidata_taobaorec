fr = open('E:/tianchi/qu.txt','r')
fw = open('E:/tianchi/test2.txt','w')
r=fr.readline()
i=0
while r!='':
    d = r.split(',')
    m = len(d)
    if m==5:
        a=d[0:2]
        b=d[2:]
        #print(b)
        b.pop()
        b.sort()
        #print(b)
        c=a+b
        newline=','.join(c)
        newline=newline+'\n'
        fw.write(newline)
    elif m==6:
        a=d[0:2]
        b=d[2:]
        #print(b)
        b.pop()
        b.sort()
        #print(b)
        c=a+b
        newline=','.join(c)
        newline=newline+'\n'
        fw.write(newline)
    r = fr.readline()
fr.close()
fw.close()
