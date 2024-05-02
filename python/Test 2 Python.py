for _ in range(int(input())):
    n=int(input())
    res=0
    for i in range(n):
        a=int(input())
        res^=a
    print(res)