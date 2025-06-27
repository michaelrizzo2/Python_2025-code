#This will help us find the missing number

def missing_number_funder(numbers:[list]) -> int:
    for number in range(min(numbers),max(numbers)+1):
        if number in numbers:
            print(f"Number {number} has been found")
        else:
            print(f"Number {number} is missing")
    print("====================================================")


missing_number_funder([3, 0, 1])
missing_number_funder([0, 1, 2, 4, 5])