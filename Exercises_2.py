def main():
    while True:

        inches = float(input("Enter a value in inches (negative value to quit): "))

        if inches < 0:
            print("Negative value entered. Program ends.")
            break

        # Convert inches to centimeters
        centimeters = inches * 2.54
        print(f"{inches} inches is equal to {centimeters} centimeters.")

if __name__ == "__main__":
    main()
