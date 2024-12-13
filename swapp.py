def swap(a,b):
    print("value of a=",a)
    print("value of b=",b)
    return b,a
a=int(input("enter a:"))
b=int(input("enter b:"))
a,b=swap(a,b)
print("value of a after swap=",a)
print("value of b after swap=",b)
