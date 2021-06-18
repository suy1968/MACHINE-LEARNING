fr = open("instance.txt",'r')
a = fr.readline()
a = a.split(' ')
hypo = [None]*(len(a) - 2)
a = fr.readlines()
for ex in a:
    ex = ex.split(' ')
    if(ex[-1] == "YES" or ex[-1] == "YES\n"):
        for i in range(len(ex) - 2):
            if(hypo[i] == None or hypo[i] == ex[i + 1]):
                hypo[i] = ex[i + 1]
            else:
                hypo[i] = '?'
print(hypo)
