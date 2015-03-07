class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        
        count = 0
        isMajority = False
        whatIsMajority = 0
        
        for index in xrange(0,len(num)):
            if not isMajority:
                whatIsMajority = num[index]
                count += 1
                isMajority = True
            elif isMajority and whatIsMajority == num[index]:
                count += 1
            #elif not isMajority and not count:
            #    isMajority = True
            #    count += 1
            #    whatIsMajority = num[index]
            elif isMajority and whatIsMajority != num[index]:
                count -= 1
                if count == 0:
                    isMajority = False
                    whatIsMajority = 0
        
        return whatIsMajority 
                    
            
        
        