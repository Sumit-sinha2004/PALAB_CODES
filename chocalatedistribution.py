class Solution:
    def findMinDiff(self, arr,M):

        # code here
        n = len(arr)
        
        if M > n:
            return -1   
        
        arr.sort()
        ans = float('inf')
        
        for i in range(n - M + 1):
            ans = min(ans, arr[i + M - 1] - arr[i])
        
        return ans
