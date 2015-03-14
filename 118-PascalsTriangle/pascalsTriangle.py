import math

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        ans = []
        
        for row in xrange(0,numRows):
            smallAns = []
            for i in xrange(0,row+1):
                smallAns.append(math.factorial(row)/(math.factorial(i)*math.factorial(row-i)))
            ans.append(smallAns)
        
        return ans
        
        