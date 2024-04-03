/*79. Word Search
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
https://assets.leetcode.com/uploads/2020/11/04/word2.jpg
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
https://assets.leetcode.com/uploads/2020/10/15/word3.jpg
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
*/
class Solution {
    public boolean exist(char[][] board, String word) {
        int m = board.length;
        int n = board[0].length;
        char[] wrd = word.toCharArray();
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dfs(board, wrd, i, j, 0))
                    return true;
            }
        }
        return false;
    }
    
    private boolean dfs(char[][] board, char[] word, int i, int j, int index) {
        if (index == word.length)
            return true;
        
        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length || board[i][j] != word[index])
            return false;
        
        char temp = board[i][j];
        board[i][j] = ' '; // Mark as visited
        
        boolean found = dfs(board, word, i + 1, j, index + 1) ||
                        dfs(board, word, i - 1, j, index + 1) ||
                        dfs(board, word, i, j + 1, index + 1) ||
                        dfs(board, word, i, j - 1, index + 1);
        
        board[i][j] = temp; // Reset the cell
        
        return found;
    }
}
