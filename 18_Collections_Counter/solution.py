from collections import Counter
n=int(input());shoes=Counter(map(int,input().split()));m=int(input());earn=0
for _ in range(m):s,p=map(int,input().split());
 if shoes[s]>0: earn+=p; shoes[s]-=1
print(earn)