def second_largest(numbers):
    first = (0)
    second = ()
    for i in numbers:
        if i > first:
            second = first
            first = i
        elif i > second:
            second = i
    return second

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("The second largest number is: ", second_largest(numbers))
