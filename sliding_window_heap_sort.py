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
