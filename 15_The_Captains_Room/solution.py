k=int(input());arr=list(map(int,input().split()));
from collections import Counter
for x,c in Counter(arr).items():
 if c==1: print(x)