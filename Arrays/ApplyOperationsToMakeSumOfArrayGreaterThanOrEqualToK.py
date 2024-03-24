'''
100228. Apply Operations to Make Sum of Array Greater Than or Equal to k
User Accepted:6863
User Tried:9833
Total Accepted:7054
Total Submissions:18892
Difficulty:Medium

You are given a positive integer k. Initially, you have an array nums = [1].
You can perform any of the following operations on the array any number of times (possibly zero):
Choose any element in the array and increase its value by 1.
Duplicate any element in the array and add it to the end of the array.
Return the minimum number of operations required to make the sum of elements of the final array greater than or equal to k.

Example 1:
Input: k = 11
Output: 5

Explanation:
We can do the following operations on the array nums = [1]:
Increase the element by 1 three times. The resulting array is nums = [4].
Duplicate the element two times. The resulting array is nums = [4,4,4].
The sum of the final array is 4 + 4 + 4 = 12 which is greater than or equal to k = 11.
The total number of operations performed is 3 + 2 = 5.

Example 2:
Input: k = 1
Output: 0

Explanation:
The sum of the original array is already greater than or equal to 1, so no operations are needed.

Constraints:

1 <= k <= 105
'''
class Solution(object):
    def minOperations(self, k):
        """
        :type k: int
        :rtype: int
        """
        nums=[1]
        count=0
        if sum(nums)==k:
            return count
        else:
            while sum(nums)<=k:
                if sum(nums)>=k:
                    break
                nums=[ele+1 for ele in nums]
                count+=1
                if sum(nums)>=k:
                    break
                nums.append(nums[0])
                count+=1
        return count      
