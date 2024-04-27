'''3128. Right Triangles
You are given a 2D boolean matrix grid.
Return an integer that is the number of right triangles that can be made with the 3 elements of grid such that all of them have a value of 1.

Note:
A collection of 3 elements of grid is a right triangle if one of its elements is in the same row with another element 
and in the same column with the third element. The 3 elements do not have to be next to each other.
 

Example 1:
Input: grid = [[0,1,0],[0,1,1],[0,1,0]]
Output: 2

Explanation:
There are two right triangles.

Example 2:
1	0	0	0
0	1	0	1
1	0	0	0
Input: grid = [[1,0,0,0],[0,1,0,1],[1,0,0,0]]
Output: 0

Explanation:
There are no right triangles.

Example 3:
Input: grid = [[1,0,1],[1,0,0],[1,0,0]]
Output: 2

Explanation:
There are two right triangles.
'''
class Solution(object):
    def numberOfRightTriangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        c = 0
        row = defaultdict(int)
        col = defaultdict(int)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    c += (row[i] - 1) * (col[j] - 1)
        return c
                    
                
        
