students=[]
for _ in range(int(input())): students.append([input(),float(input())])
low=sorted(set(s[1] for s in students))[1]
print('\n'.join(sorted(s[0] for s in students if s[1]==low)))