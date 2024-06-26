n1=int(input("enter the number1:))
n2=int(input("enter the number2:"))
operator=input("enter operator(+,-,/,%,*,):")
if operator =="+":
    print(n1+n2)
elif operator=="-":
    print(n1-n2)
elif operator=="/":
    print(n1/n2)
elif operator=="%":
    print(n1%n2)
elif operator=="*":
    print(n1*n2)
else:
    print("invalid operator")
