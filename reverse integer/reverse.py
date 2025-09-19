class Solution:
    def reverse(self, x: int) -> int:

        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Get the sign of x
        sign = -1 if x < 0 else 1

        # Reverse the absolute value of x
        reversed_num = int(str(abs(x))[::-1]) * sign

        # Check for overflow
        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0
        return reversed_num
    
s = Solution()
print(s.reverse(123))    
print(s.reverse(-123))   
print(s.reverse(1534236469))  
