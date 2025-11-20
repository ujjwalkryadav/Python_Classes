# print("Jai_sri_ram")
num = int(input("Enter a number: "))
match num:
    case 0:
        print("Number is zero")
    case _:
        match num % 2:
            case 0:
                print(num, "is Even")
            case 1:
                print(num, "is Odd")