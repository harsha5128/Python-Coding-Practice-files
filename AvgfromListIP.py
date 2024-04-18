def average():
    numbers = list(map(int,input("Enter a list of numbers separated by space: ").split()))
    total = sum(numbers)
    length = len(numbers)
    avg = total / length
    return avg

print(average())

