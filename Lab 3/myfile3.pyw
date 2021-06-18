fh = open('myfile2.pyw','r')
ans = 0
for i in fh.readlines():
    if('write' in i):
        ans += 1
print(ans)
