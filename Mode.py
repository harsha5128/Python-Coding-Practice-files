from collections import Counter

def find_mode(numbers):
    count = Counter(numbers)
    mode = count.most_common()
    return mode[0][0]

numbers = [1, 2, 3, 2, 4, 1, 2, 5, 2, 1, 6, 2]
print("The mode of the numbers is: ", find_mode(numbers))