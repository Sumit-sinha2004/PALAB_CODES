class Solution:
    def threeWayPartition(self, arr, a, b):
        i = 0
        j = 0
        k = len(arr) - 1
        
        while j <= k:
            if arr[j] < a:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j += 1
            
            elif arr[j] > b:
                arr[j], arr[k] = arr[k], arr[j]
                k -= 1
            
            else:
                j += 1
