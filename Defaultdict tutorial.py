from collections import defaultdict
n,m=map(int,input().split())
d=defaultdict(list)
for i in range(1,n+1):
    w=input()
    d[w].append(i)
for k in range(m):
    w1=input()
    if w1 in d:
        for i in d[w1]:
            print(i,end=" ")
        print()
    else:
        print(-1)
