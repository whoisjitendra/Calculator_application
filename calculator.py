while(True):
    n1=int(input('Enter the first number to complete the operation->'))
    n2=int(input('Enter the second number to complete the operation->'))
    print("1-> Addition \n2-> Substraction \n3-> Multiplication \n4-> Division")
    Choice=int(input())
    if Choice==1:
        print("Addition is :" , n1+n2)
    elif Choice==2:
        print("Substraction is :" , n1-n2)
    elif Choice==3:
        print("Multiplication is :" , n1*n2)
    elif Choice==4:
        print("Division is :" , n1/n2)
    else:
        print("Enter choose the number given above:1->4 ?????? please choose correct option:")
        
    Output=input("Do you Continue this operation?(y/n):")        
    Output=Output.lower()
    if Output!="y":
        break
    
print("Thank-you")    
    