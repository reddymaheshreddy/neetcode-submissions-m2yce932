from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False  # Handle edge cases with empty matrix
        
        # Binary search over the rows
        oL = 0
        oR = len(matrix) - 1
        
        while oL <= oR:
            mid = (oL + oR) // 2
            
            # Check if the target is within the range of the row
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                # Perform binary search in this row
                l, r = 0, len(matrix[mid]) - 1
                while l <= r:
                    m = (l + r) // 2
                    if target == matrix[mid][m]:
                        return True
                    elif target > matrix[mid][m]:
                        l = m + 1
                    else:
                        r = m - 1
                return False  # Target not found in the row
            elif target < matrix[mid][0]:
                oR = mid - 1
            else:
                oL = mid + 1
        
        return False  # Target not found in any row
