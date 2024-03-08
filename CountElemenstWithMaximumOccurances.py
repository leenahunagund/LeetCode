'''3005. Count Elements With Maximum Frequency
You are given an array nums consisting of positive integers.
Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
The frequency of an element is the number of occurrences of that element in the array.

Example 1:
Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4.

Example 2:
Input: nums = [1,2,3,4,5]
Output: 5
Explanation: All elements of the array have a frequency of 1 which is the maximum.
So the number of elements in the array with maximum frequency is 5.

#my soln, 328/623 test cases passed
class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        nums.sort()
        if len(nums)==1:
            return len(nums)
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                count+=2
            elif i==len(nums)-1 and count==0:
                return len(nums)
            else:
                continue
        return count'''

#using dictionary, 18ms beats 89.9% people, 11.63mb beats 77.01 users w python
class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mp={}
        for num in nums:
            mp[num]=mp.get(num,0)+1
        count=0
        max_freq=float('-inf')
        for freq in mp.values():
            max_freq=max(max_freq,freq)
        for freq in mp.values():
            if freq==max_freq:
                count+=max_freq
        return count
        
