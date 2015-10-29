import os
#删除多余的类目的函数
def deleteExtra(d):
    #新建一个链表
    newitem = []
    #判断链表的每个值是否含有逗号，中文逗号
    for segment in d:
        #如果没有逗号直接添加到新链表中，没有再根据逗号分隔开并将
        #分开的第一个链表值添加到新链表里
        if ','not in segment:
            newitem.append(segment)
        else:
            dsegment = segment.split(',')
            newitem.append(dsegment[0])
    #if '\n' not in newitem:
        #newitem.append('\n')
    print (newitem)
    #将新链表用分号连接起来
    newline =';'.join(newitem)
    #判断新组成的数据中是否有换行符
    if newline.find('\n')>0:
        fw.write(newline)
    else:
        newline = newline+'\n'
        fw.write(newline)       
    return 'ok'
fr = open('e:/tianchi/datanew/dim_fashion_match.txt','r')
fw = open('e:/tianchi/datanew/test0.txt','w')
r=fr.readline()
while r!='':
    #该句话里面没有逗号直接写到文件里面
    if ',' not in r:
        fw.write(r)
    else :
        #有逗号的话，把分号之间的分开
        d = r.split(';')
        deleteExtra(d)
    r = fr.readline()
fr.close()
fw.close()
