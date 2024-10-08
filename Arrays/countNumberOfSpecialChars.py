'''3120. Count the Number of Special Characters I
You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.
Return the number of special letters in word.

Example 1:
Input: word = "aaAbcBC"
Output: 3

Explanation:
The special characters in word are 'a', 'b', and 'c'.

Example 2:
Input: word = "abc"
Output: 0

Explanation:
No character in word appears in uppercase.

Example 3:
Input: word = "abBCab"

Output: 1
Explanation:
The only special character in word is 'b'.

 

Constraints:

1 <= word.length <= 50
word consists of only lowercase and uppercase English letters.
'''
class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        count=0
        seen=[]
        for ele in word:
            if ele.upper() in word and ele not in seen and ele!=ele.upper() or ele!=ele.lower() and ele==ele.lower():
                count+=1
                seen.append(ele)
        return count
                
