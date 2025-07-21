N=int(input())
result="P"
for i in range(2,N):
    if N%i==0:
        result="C"
print(result)
    