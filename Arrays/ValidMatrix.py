'''You are given two arrays rowSum and colSum of non-negative integers where rowSum[i] 
is the sum of the elements in the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix.
In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum requirements.

Return a 2D array representing any matrix that fulfills the requirements. It's guaranteed that at least one matrix that fulfills the requirements exists.

Example 1:

Input: rowSum = [3,8], colSum = [4,7]
Output: [[3,0],
         [1,7]]
Explanation: 
0th row: 3 + 0 = 3 == rowSum[0]
1st row: 1 + 7 = 8 == rowSum[1]
0th column: 3 + 1 = 4 == colSum[0]
1st column: 0 + 7 = 7 == colSum[1]
The row and column sums match, and all matrix elements are non-negative.
Another possible matrix is: [[1,2],
                             [3,5]]
Example 2:

Input: rowSum = [5,7,10], colSum = [8,6,8]

Output: [[0,5,0],
         [6,1,0],
         [2,0,8]]


         
r=[[0]*len(colSum)]*len(rowSum)
        for i in range(len(r)):
            for j in range(len(r[0])):
                if rowSum[i]<=colSum[j]:
                        r[i][j]=rowSum[i]
                        colSum[j]=colSum[j]-rowSum[i]
                        rowSum[i]=0
                elif colSum[j]<=rowSum[i]:
                    r[i][j]=colSum[j]
                    rowSum[i]=rowSum[i]-colSum[j]                        
                    colSum[j]=0
        return r'''
class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        r = [[0] * len(colSum) for _ in range(len(rowSum))]
        for i in range(len(r)):
            for j in range(len(r[0])):
                if rowSum[i] <= colSum[j]:
                    r[i][j] = rowSum[i]
                    colSum[j] -= rowSum[i]
                    rowSum[i] = 0
                else:
                    r[i][j] = colSum[j]
                    rowSum[i] -= colSum[j]
                    colSum[j] = 0
        return r
                      
