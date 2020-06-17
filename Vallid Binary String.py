s = input()
q=int(input())
# Splitting at 3
subst=[s[i:i + q] for i in range(0, len(s), q)]
print(subst)
for i in subst:
    for j in i:
        if (j=='1'):
            print("0")
        elif(j=='0'):
            print("sita")
            