for _ in range(int(input())):
    n,p = input().split()
    try: print(int(n)//int(p))
    except Exception as e:
        print("Error Code: "+str(e))
