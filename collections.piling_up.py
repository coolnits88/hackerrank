from collections import deque as dq
for _ in range(int(input())):
    n,d,top,ret = input(),dq(list(map(int,input().split()))),[],False
    while d:
        tp = d.popleft() if d[0] > d[-1] else d.pop() 
        if not top:
            top.append(tp)
        elif top[-1] >= tp:    
            top.append(tp)
        else:
            ret = True
            break
    print('No' if ret else 'Yes')
