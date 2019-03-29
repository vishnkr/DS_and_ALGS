// Problem Link - https://leetcode.com/problems/find-pivot-index/

#include<numeric>

class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        if(nums.empty()) return -1;
        int sum = std::accumulate(nums.begin(), nums.end(), 0);
        int leftsum=0;
        int num_size=nums.size();
        for(int i=0;i<=num_size;i++){
            if(sum-leftsum-nums[i]==leftsum) return i;
            leftsum+=nums[i];
        }  
        return -1; 
        
    }
};