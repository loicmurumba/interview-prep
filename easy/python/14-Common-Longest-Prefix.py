class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """ 
        common = ""
        if strs == []: 
            return common
        for index in range(len(strs[0])):
            cur = strs[0][0:index]
            for a in strs:
                if a[0:index] != cur:
                    return common
            common = cur
        return common



sol = Solution()
print(sol.longestCommonPrefix(["aaa","a","aab"]))