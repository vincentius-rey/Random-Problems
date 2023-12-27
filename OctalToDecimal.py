#Write a program to Convert Numbers from Octal to Decimal

def OctalToDecimal(octal):
    decimal = 0
    exponent = 0
    
    while octal>0:
        remainder = octal % 10
        decimal += remainder * (8**exponent)
        octal //= 10
        exponent += 1

    return decimal

while True:
    octal = int(input("Enter octal: "))
    print("Equivalent Decimal: {}" .format(OctalToDecimal(octal)))
    break

    # If you want to loop the program, just remove the quotation marks
    '''choice = input("Do you want to continue? (Y/N): ")
    
    if choice.upper() == "Y":
        print()
        continue
    elif choice.upper() == "N":
        print("Thank You!")
        break
    else:
        print("Invalid input!\n**Program Terminated**")
        break'''


    
        
