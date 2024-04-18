def longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

words = ["cat", "dog", "elephant", "giraffe", "kangaroo"]
print(longest_word(words))