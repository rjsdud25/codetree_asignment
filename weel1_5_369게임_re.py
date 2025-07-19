N=int(input())
for i in range(1,N+1,1):
    s_i=str(i)
    if ("3" in s_i or "6" in s_i or "9" in s_i):
        print(0, end=" ")
    elif i%3==0:
        print(0, end=" ")
    else:
        print(i, end=" ")