fr = open("instance.txt",'r')
a = fr.readline()
hypo = []
a = fr.readlines()
for ex in a:
    ex = ex.split(' ')
    if(ex[-1] == "YES" or ex[-1] == "YES\n"):
        if(len(hypo) == 0):
            for j in ex[1:-1]:
                hypo.append(j)
        else:
            print('Already Filled')
            for j in range(len(hypo)):
                if hypo[j] != ex[j + 1]:
                    hypo[j] = '?'
print(hypo)
