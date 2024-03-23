'''
You are given an integer array nums containing positive integers.
We define a function encrypt such that encrypt(x) replaces every digit in x with the largest digit in x. For example, encrypt(523) = 555 and encrypt(213) = 333.
Return the sum of encrypted elements.

Example 1:
Input: nums = [1,2,3]
Output: 6
Explanation: The encrypted elements are [1,2,3]. The sum of encrypted elements is 1 + 2 + 3 == 6.

Example 2:
Input: nums = [10,21,31]
Output: 66
Explanation: The encrypted elements are [11,22,33]. The sum of encrypted elements is 11 + 22 + 33 == 66.

Constraints:
1 <= nums.length <= 50
1 <= nums[i] <= 1000

class Solution(object):
    def sumOfEncryptedInt(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r=[]
        for i in range(len(nums)):
            if nums[i]<10:
                r.append(nums[i])
            elif nums[i]==10:
                nums[i]+=1
                r.append(nums[i])
            else:
                if nums[i]>10:
                    nums[i]=nums[i]//10
                    nums[i]=nums[i]*10
                    nums[i]=nums[i]+(nums[i]//10)
                    r.append(nums[i])
        return sum(r)
'''
class Solution(object):
    def sumOfEncryptedInt(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r=[]
        for i in range(len(nums)):
            if nums[i]<10:
                r.append(nums[i])
            elif nums[i]==10:
                nums[i]+=1
                r.append(nums[i])
            else:
                temp= list(map(int, str(nums[i])))
                x=max(temp)
                for j in range(len(temp)):
                    temp[j]=x
                nums[i] = int(''.join(map(str,temp)))
                r.append(nums[i])
        return sum(r)
                
                
        
        
        
