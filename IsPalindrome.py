import re
def is_palindrome(string):
    # remove special characters and spaces
    string = re.sub(r'[^A-Za-z0-9]+', '', string)
    # convert to lowercase
    string = string.lower()
    # check if the string is equal to its reverse
    return string == string[::1]

string = input("Enter a string: ")
if is_palindrome(string):
    print(string, "is a palindrome.")
else:
    print(string, "is not a palindrome.")
