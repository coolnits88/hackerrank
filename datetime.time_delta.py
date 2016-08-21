from datetime import datetime as dt

FMT = "%a %d %b %Y %H:%M:%S %z"
for _ in range(int(input())) :
    t1 = dt.strptime(input(), FMT)
    t2 = dt.strptime(input(), FMT)
    print(abs(int((t1-t2).total_seconds())))
