class Solution:
    def ispalindrome(self, s) :
        new = ''
        for a in s:
            if a.isalpha() or a.isdigit():
                new += a.lower()
        return (new == new[::-1])

sol = Solution()
s= input("Enter a string Valiue:")
print(sol.ispalindrome(s))  
print(sol.ispalindrome("race a car")) 