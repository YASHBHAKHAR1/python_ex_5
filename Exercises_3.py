def main():

    smallest = None
    largest = None

    while True:
        user_input = input("Enter a number (or press Enter to quit): ")

        if user_input == "":
            break

        number = float(user_input)


        if smallest is None or number < smallest:
            smallest = number

        if largest is None or number > largest:
            largest = number


    if smallest is not None and largest is not None:
        print(f"The smallest number entered is: {smallest}")
        print(f"The largest number entered is: {largest}")
    else:
        print("No numbers were entered.")

if __name__ == "__main__":
    main()
