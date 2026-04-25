class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        
        if not s or not t:
            return ""
        
        need = Counter(t)   # frequency of chars in t
        window = {}
        
        have = 0
        need_count = len(need)
        
        res = [-1, -1]
        res_len = float('inf')
        
        left = 0
        
        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1
            
            if ch in need and window[ch] == need[ch]:
                have += 1
            
            # Shrink window
            while have == need_count:
                # Update result
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                
                # Remove left char
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                
                left += 1
        
        l, r = res
        return s[l:r+1] if res_len != float('inf') else ""
