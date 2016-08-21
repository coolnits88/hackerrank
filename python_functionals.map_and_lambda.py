f = lambda x : x if x<2 else f(x-1) + f(x-2)
print(list(map(lambda x:x**3,map(f,range(int(input()))))))
