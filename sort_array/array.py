class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)

        # Helper: heapify function
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and arr[left] > arr[largest]:
                largest = left
            if right < n and arr[right] > arr[largest]:
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(nums, n, i)

        # Extract elements one by one
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]  
            heapify(nums, i, 0)

        return nums
    
s = Solution()
print(s.sortArray([5, 2, 3, 1]))  
print(s.sortArray([5, 1, 1, 2, 0, 0])) 
