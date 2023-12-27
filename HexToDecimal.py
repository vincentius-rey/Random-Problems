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
        

hexa = input("Enter Hexadecimal: ")
print(HexToDec(hexa))
