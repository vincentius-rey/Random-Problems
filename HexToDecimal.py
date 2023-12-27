#Write a program to Convert Numbers from Hexadecimal to Decimal

def HexToDec(hexa):
    decimal = 0
    exponent = 0

    sym = ["A", "B", "C", "D", "E", "F"]
    val = [10, 11, 12, 13, 14, 15, 16]

    for j in hexa[::-1]:
        if j in sym:
            decimal+= val[sym.index(j)]*16**exponent
            exponent+=1
        else:
            decimal += int(j)*16**exponent
            exponent+=1
    return decimal
        
while True:
    hexa = input("Enter Hexadecimal: ")
    print(HexToDec(hexa))
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
