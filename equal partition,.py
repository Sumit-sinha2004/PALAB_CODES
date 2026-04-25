class Solution:
    def equalPartition(self, arr):
        n = len(arr)
        total = sum(arr)
        
        target = total // 2
        
        # possible sizes
        sizes = [n // 2]
        if n % 2 != 0:
            sizes.append(n // 2 + 1)
        
        res = []
        
        def backtrack(start, path, curr_sum, size):
            # If valid subset found
            if len(path) == size:
                if curr_sum == target:
                    res.extend(path)
                    return True
                return False
            
            for i in range(start, n):
                # pruning
                if curr_sum + arr[i] > target:
                    continue
                
                if backtrack(i + 1, path + [arr[i]], curr_sum + arr[i], size):
                    return True
            
            return False
        
        # Try both possible sizes
        for size in sizes:
            if backtrack(0, [], 0, size):
                break
        
        subset1 = res
        subset2 = arr[:]
        
        # remove subset1 elements from subset2
        for x in subset1:
            subset2.remove(x)
        
        return [subset1, subset2]
