class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        if(nums.size()<3) return result;//不足3个元素，返回空
        sort(nums.begin(),nums.end());//排序
        const int target = 0;
        int a,b,c;//3个元素的下标
        for(a=0;a<nums.size()-2;a++){
            b=a+1;
            c=nums.size()-1;
            if(a>0 && nums[a]==nums[a-1])           continue;//跳过重复
            if(nums[a]+nums[a+1]+nums[a+2]>target)  break;//太大了
            if(nums[a]+nums[c]+nums[c-1]<target)    continue;//太小了
            while(b<c){
                int sum=nums[a]+nums[b]+nums[c];
                if(sum<target){
                    b++;
                    while(b<c && nums[b]==nums[b-1])    b++;//跳过重复
                }else if(sum>target){
                    c--;
                    while(b<c && nums[c]==nums[c+1])    c--;//跳过重复
                }else{
                    result.push_back({nums[a],nums[b],nums[c]});//得到一个解
                    b++;c--;
                    while(b<c && nums[c]==nums[c+1])    c--;//跳过重复
                    while(b<c && nums[b]==nums[b-1])    b++;//跳过重复
                }
            }
        }
        return result;
    }
};
