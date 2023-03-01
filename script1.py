msg = input("enter the message : ")
print("1. Encrypt to decimal")
print("2. Encrypt to binary")
print("3. Encrypt to octal")
print("4. Encrypt to hexadecimal")
choices = int(input("Insert choices (1-4) : "))

convert = ""

if choices == 1:
    for i in msg:
        dec_char = str(int(ord(i)))
        convert += dec_char
    print("message = ", msg)
    print("after encrypt = ", convert)
elif choices == 2:
    for i in msg:
        bin_char = bin(ord(i))[2:]
        convert += bin_char
    print("message = ", msg)
    print("after encrypt = ", convert)
elif choices == 3:
    for i in msg:
        oct_char = oct(ord(i))[2:]
        convert += oct_char
    print("message = ", msg)
    print("after encrypt = ", convert)
elif choices == 4:
    for i in msg:
        hex_char = hex(ord(i))[2:]
        convert += hex_char
    print("message = ", msg)
    print("after encrypt = ", convert)
else:
    print("Invalid choices!!!")