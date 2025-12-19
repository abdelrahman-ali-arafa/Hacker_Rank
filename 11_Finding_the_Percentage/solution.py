n=int(input());d={};
for _ in range(n):a=input().split();d[a[0]]=list(map(float,a[1:]));q=input();print(f'{sum(d[q])/len(d[q]):.2f}')