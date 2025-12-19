a=int(input());A=set(map(int,input().split()));
for _ in range(int(input())):
 c=input().split();B=set(map(int,input().split()));eval('A.'+c[0]+'(B)');print(sum(A))