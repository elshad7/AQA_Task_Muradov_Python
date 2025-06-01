def number_check():
    try:
        user_input = int(input("Enter a number: "))
        if user_input > 7:
            print("Hello")
    except ValueError:
        print("Please enter a valid number.")

def name_check():
    name = input("Enter a name: ")
    if name == "John":
        print("Hello, John")
    else:
        print("There is no such name")

def filter_multiples_of_three():
    try:
        raw_input = input("Enter numbers separated by spaces: ")
        numbers = list(map(int, raw_input.split()))
        for num in numbers:
            if num % 3 == 0:
                print(num)
    except ValueError:
        print("Please enter valid integers only")

def main():
    print("Task 1: Number check")
    number_check()
    
    print("\nTask 2: Name check")
    name_check()
    
    print("\nTask 3: Filter multiples of 3")
    filter_multiples_of_three()

if __name__ == "__main__":
    main()
