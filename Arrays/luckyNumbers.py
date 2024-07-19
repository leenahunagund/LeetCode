'''1380. Lucky Numbers in a Matrix
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

Example 1:
Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]

Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 2:
Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 3:
Input: matrix = [[7,8],[1,2]]
Output: [7]
Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.
'''
class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        '''r=len(matrix)
        c=len(matrix[0])
        transpose=[[0]*c]*r
        res=[]
        transpose=[[matrix[i][j] for i in range(r) ] for j in range(c)]

        for i in range(r):
            ele=min(matrix[i])
            if ele==max(transpose[i]):
                break
        res.append(ele)
        return res'''
        min_in_rows = {min(row) for row in matrix}  # Set of minimums from each row
        max_in_columns = {max(column) for column in zip(*matrix)}  # Set of maximums from each column

        # The intersection of these two sets will give us the lucky numbers
        lucky_numbers = list(min_in_rows & max_in_columns)
        return lucky_numbers
        
        
