import  calendar as c 
c.setfirstweekday(0)
t = list(map(int,input().strip().split()))
print(c.day_name[c.weekday(t[2],t[0],t[1])].upper())
