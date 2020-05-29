n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
print(arr)
n=arr.reverse()
print(list(n))



