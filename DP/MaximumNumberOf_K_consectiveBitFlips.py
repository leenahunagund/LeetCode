'''
LEETCODE HARD 89/113 test cases passed.. Time limit exceeded
class Solution(object):
    def minKBitFlips(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        for i in range(len(nums)):
            if nums[i]==0:
                if (k+i)<=len(nums):
                    count+=1
                for n in range(i,k+i):
                    if (k+i)<=(len(nums)):
                        if nums[n]==0:
                            nums[n]=1
                        elif nums[n]==1:
                            nums[n]=0
                    else:
                        return -1
            else: 
                continue
        return count'''
class Solution(object):
    def minKBitFlips(self, nums, k):
        n = len(nums)
        flipped = 0
        res = 0
        isFlipped = [0] * n
        
        for i in range(n):
            if i >= k:
                flipped ^= isFlipped[i - k]
            if flipped == nums[i]:
                if i + k > n:
                    return -1
                isFlipped[i] = 1
                flipped ^= 1
                res += 1
        
        return res
        
