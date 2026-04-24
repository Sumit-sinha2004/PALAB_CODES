class Solution:
    def reverseArray(self, arr):
        """
        Reverses the array in-place.

        :param arr: List[int]
        :return: None (modifies the array directly)
        """
        left = 0
        right = len(arr) - 1

        while left < right:
            # Swap elements
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1


# Example usage (for testing locally)
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    sol = Solution()
    sol.reverseArray(arr)
    print("Reversed array:", arr)
