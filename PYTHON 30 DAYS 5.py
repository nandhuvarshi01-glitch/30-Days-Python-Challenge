a=float(input("Enter number:"))
b=float(input("Enter number:"))
op=input("Enter operator (+ - * /):")
if op=='+':
    print(a+b)
elif op=='-':
    print(a-b)
elif op=='*':
    print(a*b)
elif op=='/':
    print(a/b)
else:
    print("invalid")
