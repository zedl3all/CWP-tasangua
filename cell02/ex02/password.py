def main():
    password = "Python is awesome"

    Input_Pass = str(input())

    if (Input_Pass == password):
        print("ACCESS GRANTED")
        return
    print("ACCESS DENIED")

main()