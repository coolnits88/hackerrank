n,d=input(),list(map(int,input().split()))
print(all([j > 0 for j in  d])and any([str(j) == str(j)[::-1] for j in d]))
