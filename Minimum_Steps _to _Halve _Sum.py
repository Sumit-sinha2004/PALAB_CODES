import heapq

class Solution:
    def minOperations(self, arr):
        # Convert to max heap (use negative values)
        max_heap = [-x for x in arr]
        heapq.heapify(max_heap)
        
        total_sum = sum(arr)
        target = total_sum / 2
        
        operations = 0
        
        while total_sum > target:
            # Get largest element
            largest = -heapq.heappop(max_heap)
            
            half = largest / 2
            total_sum -= half
            
            heapq.heappush(max_heap, -half)
            operations += 1
        
        return operations
