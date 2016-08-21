n,k = list(map(int,input().split()))
t=[input().split() for _ in range(n)]
sk = int(input())
[print(' '.join(s)) for s in sorted(t,key=lambda x: int(x[sk]))]
