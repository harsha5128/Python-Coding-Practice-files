def second_largest(numbers):
    numbers.sort(reverse=True)
    return numbers[1]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("The second largest number is: ", second_largest(numbers))


