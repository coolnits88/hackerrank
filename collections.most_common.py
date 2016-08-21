from collections import Counter
c = Counter(input())
[print(*list(x)) for x in sorted(c.items(),key= lambda x : (-x[1],x[0]))[:3]]
