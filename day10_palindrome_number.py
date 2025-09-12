class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindrome
        if x < 0:
            return False
        
        # Convert to string and check if reversed is same
        return str(x) == str(x)[::-1]
