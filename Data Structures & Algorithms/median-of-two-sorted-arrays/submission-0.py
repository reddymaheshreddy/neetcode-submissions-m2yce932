class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        two sorted arrays 
        find median of two arrays with O(log(m+n)) complexity
        median   0 1 2 3 4 5 6 7
        nums1 = [1,3|,4,5,5,6,7,7]
        nums2 = [1,2,4,4|,5]
        take care of empty arrays
        '''
        l1 = len(nums1)
        l2 = len(nums2)
        half = (l1 + l2) // 2

        if l1 <= l2:
            search = nums1
            other = nums2
        else:
            search = nums2
            other = nums1

        low = 0
        high = len(search) - 1

        while True:
            left = (low + high) // 2
            right = half - left - 2

            left1 = search[left] if left >= 0 else float("-inf")
            right1 = search[left + 1] if (left + 1) < len(search) else float("inf")

            left2 = other[right] if right >= 0 else float("-inf")
            right2 = other[right + 1] if (right + 1) < len(other) else float("inf")

            if left1 <= right2 and left2 <= right1:
                if (l1 + l2) % 2:
                    return min(right1, right2)
                return (max(left1, left2) + min(right1, right2)) / 2

            elif left1 > right2:
                high = left - 1
            else:
                low = left + 1



        