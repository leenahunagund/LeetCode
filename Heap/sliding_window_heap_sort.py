'''
You are given an array of integers nums, there is a sliding window of size k which is moving 
from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 
Example 2:

Input: nums = [1], k = 1
Output: [1]

'''
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        # create a deque to hold the indices of the elements in the sliding window
        window = deque()
        result = []
        
        # iterate through the array
        for i in range(len(nums)):
            # remove elements from the deque that are outside the window
            while window and window[0] <= i - k:
                window.popleft()
            
            # remove elements from the deque that are smaller than the current element
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            
            # add the index of the current element to the deque
            window.append(i)
            
            # add the maximum element in the window to the result list
            if i >= k - 1:
                result.append(nums[window[0]])
        
        return result
