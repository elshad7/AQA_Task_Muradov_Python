def number_check():
    try:
        number = int(input("Enter a number: "))
        if number > 7:
            print("Hello")
        else:
            print("Number is not greater than 7.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

def name_check():
    name = input("Enter a name: ")
    if name == "John":
        print("Hello, John")
    else:
        print("There is no such name")

def multiples_of_three():
    try:
        numbers = list(map(int, input("Enter numbers separated by space: ").split()))
        result = [num for num in numbers if num % 3 == 0]
        print("Multiples of 3 in the array:", result)
    except ValueError:
        print("Invalid input. Please enter a list of integers.")

def main():
    print("=== Number Check ===")
    number_check()
    
    print("\n=== Name Check ===")
    name_check()
    
    print("\n=== Multiples of 3 ===")
    multiples_of_three()

if __name__ == "__main__":
    main()
