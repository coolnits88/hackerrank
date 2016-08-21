d = dict()
n,m=map(int,input().split())
for i in range(n):
    w = input()
    if w in d.keys():
        d[w].append(i+1)
    else: 
        d[w] = []
        d[w].append(i+1)
for j in range(m):
    w = input()
    if w in d.keys():
        for k in d[w]:
            print(k,end=' ')
        print('')
    else: 
        print(-1)
