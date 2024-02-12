


class Solution {
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        int ele=nums[0],count=0;
        if (nums.length==1){
            ele=nums[0];
            return ele;
        }
        for(int i=0;i<nums.length;i++)
        {
            if(ele==nums[i])
            {
                count++;
                if (count>(nums.length/2))
                break;
            }
            else if(ele!=nums[i])
            {
                ele=nums[i];
                count=1;
            }
        }
        return ele;
    }
}
