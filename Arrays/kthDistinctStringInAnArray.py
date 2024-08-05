'''2053. Kth Distinct String in an Array
A distinct string is a string that is present only once in an array.
Given an array of strings arr, and an integer k, return the kth distinct string present in arr.
If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.

Example 1:

Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"
Explanation:
The only distinct strings in arr are "d" and "a".
"d" appears 1st, so it is the 1st distinct string.
"a" appears 2nd, so it is the 2nd distinct string.
Since k == 2, "a" is returned. 

Example 2:

Input: arr = ["aaa","aa","a"], k = 1
Output: "aaa"
Explanation:
All strings in arr are distinct, so the 1st string "aaa" is returned.

Example 3:

Input: arr = ["a","b","a"], k = 3
Output: ""
Explanation:
The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".
'''
class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        '''a=[]
        count=0
        res=""
        for i in range(len(arr)):
            if arr[i] in arr[i+1:] or arr[i] in arr[:i-1]:
                continue
            else:
                count+=1
                a.append(arr[i])
        if count>=k:
            for i in range(len(a)):
                if i+1==k:
                    res=a[i]
        return res'''
        from collections import Counter
        
        # Count the frequency of each element in the array
        freq = Counter(arr)
        
        # Filter the elements that are distinct (appear exactly once)
        distinct_elements = [item for item in arr if freq[item] == 1]
        
        # Check if we have at least k distinct elements
        if len(distinct_elements) >= k:
            return distinct_elements[k-1]
        else:
            return ""
          


              
