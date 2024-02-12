'''169. Majority Element
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ele,count=nums[0],0
        if len(nums)==1:
            ele=nums[0]
            return ele
        for i in range(len(nums)):
            if ele==nums[i]:
                count+=1
                if count>len(nums)/2:
                    break
            if ele!=nums[i]:
                ele=nums[i]
                count=1
        return ele

        
