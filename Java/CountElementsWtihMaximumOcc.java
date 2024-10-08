/*3005. Count Elements With Maximum Frequency
You are given an array nums consisting of positive integers.
Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
The frequency of an element is the number of occurrences of that element in the array.

Example 1:
Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4.

Example 2:
Input: nums = [1,2,3,4,5]
Output: 5
Explanation: All elements of the array have a frequency of 1 which is the maximum.
So the number of elements in the array with maximum frequency is 5.*/


//2ms beats 74.4% 
class Solution {
    public int maxFrequencyElements(int[] nums) {
        Map<Integer, Integer> frqs= new HashMap<>();
        for(int num:nums){
            frqs.put(num,frqs.getOrDefault(num,0)+1);
        }
        int maxFreq=0,cntMaxFreq=0;
        for(int frq:frqs.values()){
            if (frq==maxFreq) cntMaxFreq++;
            else if (frq>maxFreq){
                maxFreq=frq;
                cntMaxFreq=1;
            }
        }
        return maxFreq*cntMaxFreq;
    }
}
