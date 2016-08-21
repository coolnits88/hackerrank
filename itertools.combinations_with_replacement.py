from itertools import combinations_with_replacement as cwr
x,y = input().split()
[print(''.join(c)) for c in cwr(sorted(x),int(y))]
