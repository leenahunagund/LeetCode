'''1207. Unique Number of Occurrences
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:
Input: arr = [1,2]
Output: false

Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

---my soln--- 
49/67 test cases passed 
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n=len(arr)
        arr.sort()
        count=[0]*n
        for i in range(1,n):
            if arr[i]!=arr[i-1]:
                continue
            else:
                count[i]+=1
        for i in range(len(count)):
            if count[i-1]==count[i]:
                return False
            else:
                return True '''
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n=len(arr)
        arr.sort()
        count=[]
        i=0
        while i<n:
            cnt=1
            while i+1<n and arr[i]==arr[i+1]:
                cnt+=1
                i+=1
            count.append(cnt)
            i+=1
        count.sort()
        for i in range(1,len(count)):
            if count[i-1]==count[i]:
                return False
        return True
