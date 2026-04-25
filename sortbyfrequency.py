class Solution:
    def frequencySort(self, s):
        from collections import Counter
        
        freq = Counter(s)
        
        # sort by (frequency, character)
        sorted_chars = sorted(freq.keys(), key=lambda x: (freq[x], x))
        
        result = ""
        for ch in sorted_chars:
            result += ch * freq[ch]
        
        return resul
