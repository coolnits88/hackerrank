from collections import Counter
input()
c = dict(Counter(map(int,input().split())))
sale = 0
for _ in range(int(input())):
    s,p = list(map(int,input().split()))
    if s in c and c[s] != 0:
        sale += p
        c[s] = c[s] - 1

print(sale)
        
