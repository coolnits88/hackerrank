import re
print(sorted(list(filter(lambda x: re.match(r'\b[\w-]+@[0-9A-Za-z]+\.\w{1,3}\b',x) ,[input() for _ in range(int(input()))]))))
