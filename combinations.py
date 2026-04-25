lass Solution:
    def combine(self, n: int, k: int):
        res = []
        
        def backtrack(start, path):
            # If combination size is k → add to result
            if len(path) == k:
                res.append(path[:])
                return
            
            # Try all numbers from 'start' to n
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()  # backtrack
        
        backtrack(1, [])
        return res
