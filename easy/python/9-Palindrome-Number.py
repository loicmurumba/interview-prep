class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        tmp = x
        rev = 0
        while tmp  > 0:
            rev += tmp % 10
            tmp //= 10
            rev *= 10
        rev //=10
        return rev == x
        

sol = Solution()
print(sol.isPalindrome(1101))