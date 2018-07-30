class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        if x < 0:
            x *= -1
            neg = True
        res = 0
        while x > 0:
            res += (x % 10)
            res *= 10            
            x //= 10
        res //=10
        if res > 2147483647:
            return 0
        return res if not neg else res*(-1)

sol = Solution()
print(sol.reverse(-123))