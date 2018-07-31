class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romans = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        index = 0
        total = 0
        for index,char in enumerate(s):
            if index != len(s)-1:
                if romans[s[index+1]] > romans[char]:
                    total -= romans[char]
                    continue;         
            total += romans[char]
        return total    

sol = Solution()
print(sol.romanToInt("IV"))