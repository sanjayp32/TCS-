def Index(n,x,y):
    first=-1
    last=-1
    for i in range(0,n):
        if x[i]==y and first==-1:
            first=i
            last=i
        elif x[i]==y and first!=-1:
            last=i
    if first==-1:
        print("No occurances")
    else:
        print(first,last)
n=int(input("Enter the number of elements : "))
x=list(map(int,input("Enter : ").split()))
y=int(input("Enter the element you want to search : "))
Index(n,x,y)