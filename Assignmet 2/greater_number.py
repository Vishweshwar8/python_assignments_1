def greaterNum(a,b):
    if a>b:
        print(a)
    elif b>a:
        print(b)
    else:
        print("Both Are Equal : ",a)

a = int(input("Enter number 1 : "))
b = int(input("Enter number 2 : "))
greaterNum(a,b)