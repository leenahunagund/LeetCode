'''2149. Rearrange Array Elements by Sign
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
You should rearrange the elements of nums such that the modified array follows the give conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions. 

Example 1:
Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.  

Example 2:
Input: nums = [-1,1]
Output: [1,-1]
Explanation:
1 is the only positive integer and -1 the only negative integer in nums.
So nums is rearranged to [1,-1].


class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        e=[]
        o=[]
        r=[]
        for i in range(len(nums)):
            if nums[i]>0:
                e.append(nums[i])
            else:
                if nums[i]<0:
                    o.append(nums[i])
        for i in range(len(nums)):
            if i%2==0:
                x=e.pop(0)
                r.append(x)
            else:
                if i%2==1:
                    y=o.pop(0)
                    r.append(y)
        return r
'''
#same but modified ,1084 ms(beats 99.75% users w python), 44.30Mb(beats 79.40 users with python
class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r=[-1]*(len(nums))
        e=0
        o=1
        for i in nums:
            if i>0:
                r[e]=i
                e+=2
            else:
                r[o]=i
                o+=2
        return r
                

            
        
            
        
