class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def quicksort(left, right):
            if left >= right:
                return

            # Partition
            pivot = nums[(left + right) // 2]  # choose middle element as pivot
            i, j = left, right

            while i <= j:
                while nums[i] < pivot:
                    i += 1
                while nums[j] > pivot:
                    j -= 1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]  # swap
                    i += 1
                    j -= 1

            # Recurse
            quicksort(left, j)
            quicksort(i, right)

        quicksort(0, len(nums) - 1)
        return nums
