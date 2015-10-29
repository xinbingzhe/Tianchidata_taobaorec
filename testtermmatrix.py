from count_term_match import count_term_match    
fr1 = open('E:/tianchi/dataresult/datar/test/test_detail.txt','r')
fr2 = open('E:/tianchi/dataresult/datar/test/fencirules_alltxt.txt','r')
fw1 = open('E:/tianchi/dataresult/datar/test/test_termdemo.txt','w')
r1=fr1.readline()
termlist=[]
while r1!='':
    ##找每一个待测数据的term数组
    d1=r1.split(',')
    ##去掉换行符
    d1.pop()
    ##test_id为字符串
    test_id = d1[0]
    ##test_term 存放term
    test_term = d1[1:]
    r2 = fr2.readline()
    while r2!='':
        d2 = r2.split(',')
##        print(d2)
        ##去掉换行符
        d2.pop()
        ##conf为字符串
        conf = d2[-1]
##        print(conf)
        ##只留下term
        d2.pop()
        count = count_term_match(test_term,d2)
##        print(count)
        ##将在其中的个数乘以支持度
        flag = count*float(conf)
##        print(flag)
        ##转换成字符串
        str_flag = str(flag)
        ##添加到term列表中
        termlist.append(str_flag)
        r2=fr2.readline()
        ##'print (ti.cat_id)'
        ##将test_id转换成列表才能和列表连接一起
    test_item = [test_id]
    newlist = test_item+termlist
        ##用逗号连接成字符串
    newline = ','.join(newlist)
        ##加换行符
    newline =newline+'\n'
##    print (newline)
    fw1.write(newline)
    termlist=[]
    r1=fr1.readline()
    fr2.seek(0)
fr1.close()
fr2.close()
fw1.close()
