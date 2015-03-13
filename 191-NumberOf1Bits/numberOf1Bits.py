class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        
        i = 0
        j = 31
        
        while n > 0:
            if (2**j) <= n:
                break
            j -= 1
            
        while n > 0 and j>=0:
            if n % 2:
                i += 1
                n = n/2
            else:
                n = n/2
            
            j -= 1
            
        return i
        