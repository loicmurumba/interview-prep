class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()){
            return 0;
        }
        int j = 0;
        int last = nums[j]+1;
        for (int i = 0; i < nums.size(); i++) {
            if(last != nums[i]){
                last = nums[i];
                nums[j] = nums[i];
                j++;
            }   
        }
        return j;
    }
};