#include <math>

class Solution {
    
public:
    int trailingZeroes(int n) {
        int count=0;
        float index=1;
        
        while (pow(5, index) <= n) {
            count += ((int)n/(pow(5, index)));
            index += 1;
        }
        
        return count;
    }
};