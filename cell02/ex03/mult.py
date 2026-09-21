def is_neg(number):

    if (number > 0):
        print("The result is positive.")
    elif (number < 0):
        print("The result is negative.")
    else:
        print("The result is both positive and negative.")

def main():

    First_Number = int(input("Enter the first number: \n"))
    Second_Number = int(input("Enter the second number: \n"))

    Result = First_Number*Second_Number

    print(str(First_Number), "x", str(Second_Number), "=", str(Result))

    is_neg(Result)

main()
