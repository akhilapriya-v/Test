# weather_model_all_stages.py

def quadratic(a, b, c, x):
    return a * x**2 + b * x + c

def hardcoded_mode():
    print("\n--- Hardcoded Mode ---")
    a, b, c, x = 1.2, -3.4, 15.0, 5
    y = quadratic(a, b, c, x)
    print(f"Result: y = {y}")

def keyboard_input_mode():
    print("\n--- Keyboard Input Mode ---")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    x = float(input("Enter value of x: "))
    y = quadratic(a, b, c, x)
    print(f"Result: y = {y}")

def file_single_input_mode():
    print("\n--- File Input (Single Set) Mode ---")
    try:
        with open("input.txt", "r") as file:
            a = float(file.readline())
            b = float(file.readline())
            c = float(file.readline())
            x = float(file.readline())
        y = quadratic(a, b, c, x)
        print(f"Result: y = {y}")
    except Exception as e:
        print("Error reading file:", e)

def file_multiple_inputs_mode():
    print("\n--- File Input (Multiple Sets) Mode ---")
    try:
        with open("multiple_inputs.txt", "r") as file:
            for line_num, line in enumerate(file, start=1):
                a, b, c, x = map(float, line.strip().split())
                y = quadratic(a, b, c, x)
                print(f"Line {line_num}: y = {y}")
    except Exception as e:
        print("Error reading file:", e)

def main():
    while True:
        print("\nChoose Mode:")
        print("1. Hardcoded")
        print("2. Keyboard Input")
        print("3. File Input (Single Set)")
        print("4. File Input (Multiple Sets)")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            hardcoded_mode()
        elif choice == "2":
            keyboard_input_mode()
        elif choice == "3":
            file_single_input_mode()
        elif choice == "4":
            file_multiple_inputs_mode()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
