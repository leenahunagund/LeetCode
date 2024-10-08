''' 1496. Path Crossing
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', 
each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

Example 1:
Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.

Example 2:
Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.
'''
class Solution:
    def isPathCrossing(self, path):
        x, y = 0, 0
        visited = {(0, 0)}

        for direction in path:
            x += 1 if direction == 'E' else (-1 if direction == 'W' else 0)
            y += 1 if direction == 'N' else (-1 if direction == 'S' else 0)

            if (x, y) in visited:
                return True

            visited.add((x, y))

        return False
'''----my soln--- 
45/81 test cases passed
class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        N=1
        E=1
        W=-1
        S=-1
        val=0
        for i in range(len(path)):
            if len(path)==1:
                return False
            if path[i] =='N' or path[i] =='E':
                val+=1
            elif path[i]=='W' or path[i] =='S':
                val-=1
            else: 
                val=0
        if val>0:
            return False
        else:
            if val<=0:
                return True'''        


        
        
