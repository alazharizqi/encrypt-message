msg = input("enter the message : ")
print("1. encrypt to int")
print("2. encrypt to bin")
print("3. encrypt to octal")
print("4. encrypt to hex")
choices = int(input("Insert choices (1-4) : "))

convert = ""

if choices == 1:
    for i in msg:
        int_char = str(int(ord(i)))
        # print(int_char)
        convert += int_char
    print("message = ", msg)
    print("after encrypt = ", convert)
elif choices == 2:
    for i in msg:
        bin_char = bin(ord(i))[2:]
        # print(bin_char)
        convert += bin_char
    print("message = ", msg)
    print("after encrypt = ", convert)
elif choices == 3:
    for i in msg:
        oct_char = oct(ord(i))[2:]
        # print(oct_char)
        convert += oct_char
    print("message = ", msg)
    print("after encrypt = ", convert)
elif choices == 4:
    for i in msg:
        hex_char = hex(ord(i))[2:]
        # print(hex_char)
        convert += hex_char
    print("message = ", msg)
    print("after encrypt = ", convert)
else:
    print("Invalid choices!!!")