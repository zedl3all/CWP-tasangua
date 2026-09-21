def main():

    number = int(input("Enter a number less than 25 \n"))

    if (number >= 25):
        print("Error")
        return

    while number < 25+1:
        print("Inside the loop, my variable is", number)
        number += 1

main()