class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        index = 1
        count = 0
        while (5**index) <= n:
            count = count + (n/(5**index))
            index += 1
        return count
            
        