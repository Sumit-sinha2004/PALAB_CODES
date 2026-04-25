class Solution:
    def maxString(self, s, k):
        stack = []
        
        for ch in s:
            while stack and k > 0 and stack[-1] < ch:
                stack.pop()
                k -= 1
            stack.append(ch)
        
        # If k still remains, remove from end
        while k > 0:
            stack.pop()
            k -= 1
        
        return "".join(stack)
