print("\n")
print("***Welcome to Simple Calculator***")
print("This software helps you in performing simple, basic arithmetic operations.")
print("Hope you enjoy!\n")

op= input("Enter:\n1 -> Addition\n2 -> Subtraction\n3 -> Multiplication\n4 -> Division\nEnter your choice: \n")
if op in['1','2','3','4']:
    try:
        num1=float(input("Enter the First Number: "))
        num2=float(input("Enter the Second number: "))
    
        if op =='1':
            result= num1+num2
            print("\nThe sum is: ",result)
            print("\nThank you for using our program")
            
        elif op =="2":
            result= num1-num2
            print("\nThe difference is: ",result)
            print("\nThank you for using our program :)")
            
        elif op =="3":
            result= num1*num2
            print("\nThe product is: ",result)
            print("\nThank you for using our program :)")

        elif op == "4":
            if num2!=0:
                result= num1/num2
                print("\nThe quotient is: ",result)
                print("\nThank you for using our program :)")
            else:
                print("You cannot divide by zero :(")

    except ValueError:
        print("It is not a valid operator!:(\nPlease try again, make sure you enter only numbers.")
