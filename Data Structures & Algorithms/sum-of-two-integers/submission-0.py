class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF      # 32 bits
        MAX_INT = 0x7FFFFFFF   # max positive

        while b != 0:
            carry = (a & b) & MASK
            a = (a ^ b) & MASK
            b = (carry << 1) & MASK

    # handle negative numbers
        return a if a <= MAX_INT else ~(a ^ MASK)
            
        