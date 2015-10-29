i = 0
fr1 = open('E:/tianchi/dataresult/datar/dimcatmatrix/dim_catmatrix.txt','r')
fw1 = open('E:/tianchi/dataresult/datar/dimcatmatrix/splitdim_catmatrix/0.txt','w')
j = 0
k = 1
r1=fr1.readline()
while r1!='':
    fw1.write(r1)
    if i == 20000:
        fw1 = open('E:/tianchi/dataresult/datar/dimcatmatrix/splitdim_catmatrix/%s.txt'%(k),'w')
        k = k+1
        i = 0
    r1=fr1.readline()
    i = i+1
    j = j+1
fr1.close()
fw1.close()
