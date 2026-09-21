def main():
    number = float(input("Give me a number: "))

    if(number.is_integer()):
        print("This number is an integer.")
        return
    print("This number is a decimal.")
    
main()