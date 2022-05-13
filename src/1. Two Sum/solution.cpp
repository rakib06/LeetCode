class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> history;
        vector<int> result;
        for (int i = 0; i<nums.size() ; i++  ){
            int needed = target - nums[i];
            if (history.find(needed)!= history.end()){
                result.push_back(history[needed]);    
                result.push_back(i);
                return result;
            } 
            history[nums[i]] = i;  
        }
        return {};   
    }
};