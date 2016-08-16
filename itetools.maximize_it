from itertools import product as prd
k,m = map(int,input().split())
fx = [map(int,input().split()[1:]) for _ in range(k)]
print(max([sum([int(t)**2 for t in d])%m for d in prd(*fx) ]))
