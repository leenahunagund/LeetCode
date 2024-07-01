'''1550. Three Consecutive Odds
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 

Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.'''

class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        '''
        24/32 test cases
        for i in range(len(arr)):
            if arr[i]%2==1:
                if arr[i]>1:
                    if arr[i]-2 in arr and arr[i]+2 in arr:
                        return True
                elif arr[i]+2 in arr and arr[i]+4 in arr:
                    return True
                else:
                    for j in range(len(arr)-1):
                        if arr[j]==arr[j+1]:
                            return True
        return False'''
        count = 0 # Initialize count to keep track of consecutive odd numbers

        for num in arr: # Iterate through each element in the array
            if num % 2 != 0: # Check if the current element is odd
                count += 1 # Increment the count if it's odd
                if count == 3: # If we have found three consecutive odds, return true
                    return True
            else: # If the element is even, reset the count to 0
                count = 0

        return False

        
