
while True:
    a = float(input("Enter the first value "))
    b = float(input("Enter the Second value "))
    c = str(input("Enter the operator (+,-,*,/): "))
    if(c=="+"):
        print(a+b)
    elif(c=="-"):
        print(a-b)
    elif(c=="*"):
        print(a*b)
    elif(c=="/"):
        if(b==0):
            print("The value of b is zero")
        else:
            print(a/b)
    choice = input("yes or no  ")
    if(choice == "yes"):
        continue
    else:
        print("good bye")
        break
