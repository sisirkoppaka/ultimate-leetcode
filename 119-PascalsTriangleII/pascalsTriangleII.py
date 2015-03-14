class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        ans = []
        for i in xrange(0,rowIndex+1):
            ans.append(math.factorial(rowIndex)/(math.factorial(i)*math.factorial(rowIndex-i)))

        return ans
        