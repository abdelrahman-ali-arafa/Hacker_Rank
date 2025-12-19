lst=[]
for _ in range(int(input())):
 c=input().split();
 if c[0]=='print': print(lst)
 else: eval('lst.'+c[0]+'('+','.join(c[1:])+')')