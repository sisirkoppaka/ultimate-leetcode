class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        
        s = list(s)
        
        sum = 0
        
        for index, element in enumerate(s[::-1]):
            sum += (26**index)*(alphabets.index(element)+1) #+ (alphabets.index(element)+1)
        
        return sum
        
        