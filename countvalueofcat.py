from sortdict import sort_dict
fr1 = open('E:/tianchi/dataresult/datar/testcatmatrix/testcatmatrix.txt','r')
fr2 = open('E:/tianchi/dataresult/datar/dimcatmatrix/dim_catmatrix.txt','r')
fw1 = open('E:/tianchi/dataresult/datar/recdemo.txt','w')
r1=fr1.readline()
line = 0
reclist = []
while r1!='':
    if '\n' in r1:
        d1 = r1.split('\n')
        ##print (d1)
        d1.pop()
        d1 = d1[0].split(',')
    else:
        d1 = r1.split(',')
    ##test_id为字符串
    test_id = d1[0]
    ##test_term 存放term
    test_catmatrix = d1[1:]
    ##print (test_catmatrix)
    ##print ('                  ')
    r2 = fr2.readline()
    ##print (r2)
    ##print (r2)
    dic = {}
    while r2!='':
        if '\n' in r2:
            d2 = r2.split('\n')
            ##print(d2)
            d2.pop()
            ##print(d2)
            d2 = d2[0].split(',')
        else :
            d2 = r2.split(',')
            ##print (d2)
        dim_id = d2[0]
        dim_catmatrix = d2[1:]
        ##print (dim_catmatrix)
        i = 0
        count = 0.0
        while i<len(test_catmatrix) :
            ##print(test_catmatrix[i])
            f1 = float(test_catmatrix[i])
            f2 = float(dim_catmatrix[i])
            count = count + f1*f2
            i = i+1
        ##print (count)
        ##矩阵之和放入字典中
        dic[dim_id] = count
        r2=fr2.readline()
    ##print (dic)
    sortlist = sort_dict(dic)
    rec = sortlist[-200:]
    ##print ('rec:',rec)
    for r in rec:
        reclist.append(str(r[0]))
    ##print (reclist)
    test_item = [test_id]
    newlist = test_item+reclist
    newline = ','.join(newlist)
    newline =newline+'\n'
    fw1.write(newline)
    reclist=[]
    r1=fr1.readline()
    print(line)
    line = line +1
    fr2.seek(0)
fr1.close()
fr2.close()
fw1.close()
