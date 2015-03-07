class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        #version1_str = version1.split('.')
        #version2_str = version2.split('.')
        
        version1_lst = map(int, (version1.split('.')))
        version2_lst = map(int, (version2.split('.')))
        
        max_len = max(len(version1_lst),len(version2_lst))
        min_len = min(len(version1_lst),len(version2_lst))
        
        answer = -2
        
        for index in xrange(min_len):
                if version1_lst[index] > version2_lst[index]:
                    answer = 1
                    break
                
                if version1_lst[index] < version2_lst[index]:
                    answer = -1
                    break
        
        if answer == -2:
                if len(version1_lst) > len(version2_lst):
                    if sum(version1_lst[min_len:max_len]) == 0:
                        answer = 0
                        return answer
                    answer = 1
                    return answer
                    
                if len(version1_lst) < len(version2_lst):
                    if sum(version2_lst[min_len:max_len]) == 0:
                        answer = 0
                        return answer
                    answer = -1
                    return answer
                    
                answer = 0            
        
        else:
            return answer

                
        return answer
        