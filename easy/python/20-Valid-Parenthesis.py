class Stack(object):
    def __init__(self):
        self.arr = []
    def peek(self):
        return self.arr[len(self.arr)-1]
    def push(self, val):
        self.arr.append(val)
    def pop(self):
        return self.arr.pop()
    def size(self):
        return len(self.arr)
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = Stack()
        open_b = ["[","(","{"]
        close_list = ["]",")","}"]
        close_b = {"[":"]","(":")","{":"}"}
        for char in s:
            
            if char in open_b:
                stack.push(close_b[char])
            if char in close_list and stack.peek() == char:
                stack.pop()
            else:
                print(stack.peek())
                print("here")
                return False
        if stack.size() > 0:
            return False
            
sol = Solution()
print(sol.isValid("()"))