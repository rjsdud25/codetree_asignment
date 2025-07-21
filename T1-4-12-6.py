A=0
for i in range(3):
    a1,a2=input().split()
    if (a1=='Y' and int(a2)>=37): 
        A+=1
if A>=2:
    print("E")
else:
    print("N")