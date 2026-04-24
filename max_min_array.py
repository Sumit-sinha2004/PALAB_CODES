class Solution:
    def getMinMax(self, arr):
        """
        Returns minimum and maximum element of array
        :param arr: List[int]
        :return: (min, max)
        """
        if not arr:
            return None
        
        min_val = arr[0]
        max_val = arr[0]
        
        for num in arr:
            if num < min_val:
                min_val = num
            elif num > max_val:
                max_val = num
        
        return min_val, max_val


# Example usage
if __name__ == "__main__":
    arr = [3, 5, 1, 8, 2]
    
    sol = Solution()
    mn, mx = sol.getMinMax(arr)
    
    print("Minimum:", mn)
    print("Maximum:", mx)
