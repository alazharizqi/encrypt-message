print("1. int to binary")
print("2. int to octal")
print("3. int to hex")

choices = int(input("Insert choices (1-3) : "))

if choices == 1:
    number = int(input("Insert number : "))
    convert = bin(number)
    print("int = ", number)
    print("binary = ", convert)
elif choices == 2:
    number = int(input("Insert number : "))
    convert = oct(number)
    print("int = ", number)
    print("octal = ", convert)
elif choices == 3:
    number = int(input("Insert number : "))
    convert = hex(number)
    print("int = ", number)
    print("hexadecimal = ", convert)
else:
    print("Invalid choices!!!")