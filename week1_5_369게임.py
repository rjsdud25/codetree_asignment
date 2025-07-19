N=int(input())
for i in range(1,N+1,1):
    a=i//100
    b=(i-(a*100))//10
    c=(i-(a*100)-(b*10))
    if i%3==0:
        print(0,end=" ")
    elif a==3 or a==6 or a==9:
        print(0,end=" ")
    elif b==3 or b==6 or b==9:
        print(0,end=" ")
    elif c==3 or c==6 or c==9:
        print(0,end=" ")
    else:
        print(i, end=" ")    