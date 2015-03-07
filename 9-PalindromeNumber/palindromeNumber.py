class Solution:
    def extractDigit(self, x, a):
        num = x//(10**(a-1))
        return num%10
        
    # @return a boolean
    def isPalindrome(self, x):
        
        isPal = True
        isNeg = True
        
        if x < 0:
            isNeg = True
        else:
            isNeg = False
            
        x = abs(x)
        
        #digits = 1
        maxDigits = 1
        
        while (x//(10**maxDigits)) != 0:
            maxDigits += 1
        
        if isNeg is False:    
            for a in xrange(0,maxDigits//2):
                if self.extractDigit(x,a+1) != self.extractDigit(x,maxDigits-a):
                    isPal = False
                    break
        else:
            isPal = False
        
        return isPal

        