def RomanNumerals(num):
    val = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    i = len(val)-1
    while num > 0:
        quo = num // val[i]     #Gets the integer quotient of the integer
        num %= val[i]           #Gets the remainder when the integer is divided by the base number
        while quo > 0: 
            print(sym[i], end="")
            quo -= 1            # Decrements the quotient until it gets to 0
        i -= 1                  # Decrementing the index
        

number = int(input("Enter an integer: "))
RomanNumerals(number)
    

