'''1704. Determine if String Halves Are Alike
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). 
Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

Example 1:
Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

Example 2:
Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.

'''

import string
class Solution(object):
    def halvesAreAlike(self, s):
        def checkval(ele):
            al=set("aeiouAEIOU")
            if ele in al:
                return True
        """
        :type s: str
        :rtype: bool
        """
        s1=[] 
        s2=[]
        count1=0
        count2=0
        s=list(s)
        for i in range(len(s)/2):
            s1.append(s[i])
        for i in range(len(s)/2,len(s)):
            s2.append(s[i])
        for i in range(len(s1)):
            if checkval(s1[i]):
                count1+=1
        for i in range(len(s2)):
            if checkval(s2[i]):
                count2+=1
        if count1==count2:
            return True
        else:
            return False      
