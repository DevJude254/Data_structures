class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        
        original = x
        result = 0

        while x !=0:
            digit = x % 10
            x = x // 10
            result = result * 10 + digit

        if result == original:
            return True
        else:
            return False


s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))