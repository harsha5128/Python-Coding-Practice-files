def reverse_string(s):
    return s[::-1]
s=input("Please enter your string value: ")
if reverse_string(s):
    print(s, "is a palindrome.")
else:
    print(s, "is not a palindrome.")
