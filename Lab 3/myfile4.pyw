rf = open('sample.txt','r')
wf1 = open('num.txt','w')
wf2 = open('chars.txt','w')
for i in rf.readlines():
    x = i.split(' ')
    wf1.write(x[0]+'\n')
    wf2.write(x[1])
wf1.close()
wf2.close()
