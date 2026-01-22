numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def filter_even_numbers(num_list):
    result = []

    for number in num_list:
        if number % 2 == 0:
            result.append(number)

    return result


print(f"Original list: {numbers}")
print(f"List with even numbers only: {filter_even_numbers(numbers)}")