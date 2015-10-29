fr1 = open('E:/tianchi/dataresult/datar/dimcatmatrix/dimcatt.txt','r')
fr2 = open('E:/tianchi/dataresult/datar/dimcatmatrix/dimcatmademo.txt','r')
fw1 = open('E:/tianchi/dataresult/datar/dimcatmatrix/dim_catdemo.txt','w')
catlist=[]
r1=fr1.readline()
##找每一个待测数据的cat数组
while r1!='':
    ##找每一个待测数据的cat数组
    d1=r1.split(',')
    ##print(d1)
    dim_id = d1[0]
    dim_cat = d1[1]
    ##'找出testitem的cat匹配类目'
    r2=fr2.readline()
    while r2!='':
        d2=r2.split(',')
        d2.pop()
        conf = d2[-1]
        d2.pop()
        ##print(d2)
        ##看item的类目是否在类目搭配表中
        count = d2.count(d1[1])
        ##将在其中的个数乘以支持度
        flag = count*float(conf)      
        ##'print(flag)'
        ##转换成字符串
        str_flag = str(flag)
        ##添加到cat列表中
        ##print(catlist)
        catlist.append(str_flag)
        r2=fr2.readline()
        ##'print (ti.cat_id)'
        ##转换成列表
    cat_idlist=[dim_id]
    newlist = cat_idlist+catlist
        ##用逗号连接成字符串
    newline = ','.join(newlist)
        ##加换行符
    newline =newline+'\n'
    ##print (newline)
    fw1.write(newline)
    catlist=[]
    ##print('ti.catarray')
    ##print(catlist)
    r1=fr1.readline()
    ##回到fr2文件开头
    fr2.seek(0)
fr1.close()
fr2.close()
fw1.close()
