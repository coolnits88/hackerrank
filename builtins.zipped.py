n,x = list(map(int,input().split()))
i = [ list(map(float,input().split())) for _ in range(x)]
[print(round(sum(t)/x,2)) for t in zip(*i)]    
