import random
import string

def generate_password(length):
    # Create a list of possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Use the sample method of the random module to generate a list of random characters
    password = random.sample(characters, length)
    # Convert the list of characters to a string and return it
    return "".join(password)

length = int(input("Enter the desired length of the password: "))
password = generate_password(length)
print("Your password is:", password)
