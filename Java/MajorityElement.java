/*169. Majority Element
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3
    
Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2*/


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
