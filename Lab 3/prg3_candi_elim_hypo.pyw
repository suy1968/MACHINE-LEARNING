def fun(Hypo):
    if len(Hypo)>0:    
        s='{<'
        for i in Hypo:
            s+=i+','
        s=s[:-1]+'>}'
        print(s)

All_G=[]
f=open('instance2.txt','r')
Init=['0','0','0','0','0','0']
G0=['?','?','?','?','?','?']
fun(Init)
fun(G0)
Hypo=[]
for l in f.readlines():
    #print ('\n')
    a=l.split(',')
    if a[-1][:-1]=='yes':
        #print('a',a)
        if len(Hypo)==0:
            for i in a[:-1]:
                Hypo.append(i)
        else:
            for k in range(6):
                if Hypo[k]!=a[k]:
                    Hypo[k]='?'
    else:
        for k in range(6):
            NewG=G0.copy()
            if Hypo[k]!=a[k] and Hypo[k]!='?':
                NewG[k]=a[k]
                #print ('NewG',NewG)
                All_G.append(NewG)
                #fun(NewG)
                
    
        
    fun(Hypo)
    for g in All_G:
        fun(g)

for g,n in zip(All_G,range(len(All_G))):
    for i in range(6):
        if g[i]!='?' and Hypo[i]=='?':
           g[i]='?' 
    if g.count('?')==6:
               All_G.remove(g)
        
print (All_G)
                    
                
        

