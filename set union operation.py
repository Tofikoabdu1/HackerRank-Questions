n=int(input())
english=list(input().split())
m=int(input())
french=list(input().split())
eng=set(english)
fre=set(french)

print(len(eng.union(fre)))
