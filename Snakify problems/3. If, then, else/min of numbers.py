a = float(input())
b = float(input())
c = float(input())

if (a>b):
    if (b>c):
        print(c)
    else: 
        print(b)    
else: 
    if (a<c):
        print(a)
    else:
        if (b>c):
            print(c)
        else: 
            print(b)