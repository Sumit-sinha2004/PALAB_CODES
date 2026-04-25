lass Solution:
    def permute(self, arr):
        res = []
        
        def backtrack(index):
            # If we reach end → one permutation ready
            if index == len(arr):
                res.append(arr[:])
                return
            
            for i in range(index, len(arr)):
                # Swap
                arr[index], arr[i] = arr[i], arr[index]
                
                # Recurse
                backtrack(index + 1)
                
                # Backtrack (undo swap)
                arr[index], arr[i] = arr[i], arr[index]
        
        backtrack(0)
        return res
