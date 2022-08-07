from os import sep


def Pattern(x,y):
    for i in range(0,x):
        for j in range(0,y):
            if i==0 or i==x-1 or j==0 or j==y-1:
                print("1")
            else:
                print("0")
        print("\n")
x,y=map(int,input("Enter the number of rows and columns : ").split())
Pattern(x,y)