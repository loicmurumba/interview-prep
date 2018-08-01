class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ln = len(needle)
        if not ln:
            return 0
        for index in range(len(haystack)):
            if index+ln <= len(haystack):
                if haystack[index:index+ln] == needle:
                    return index;
        return -1 
sol = Solution()
print(sol.strStr("ll","ll"))