class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        prev = float("inf")
        for i in range(n - 2):
            if nums[i] == prev:
                continue

            target = -nums[i]
            low = i + 1
            high = n - 1
            prev_low = float("inf")
            prev_high = float("inf")
            pl = float("inf")
            ph=float("inf")

            while low < high:
                # skip duplicate low/high values
                if nums[low] == prev_low and nums[high] == prev_high and pl!=low and ph!=high:
                    low += 1
                    high -= 1
                    continue

                curr = nums[low] + nums[high]
                pl=low
                ph=high
                prev_low = nums[low]
                prev_high = nums[high]

                if curr == target:
                    res.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                elif curr > target:
                    high -= 1
                else:
                    low += 1

            prev = nums[i]

        return res
        