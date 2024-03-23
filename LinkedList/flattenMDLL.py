''' 430. Flatten a Multilevel Doubly Linked List
You are given a doubly linked list, which contains nodes that have a next pointer,
a previous pointer, and an additional child pointer.
This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. 
These child lists may have one or more children of their own, and so on, to produce a multilevel data structure as shown in the example below.

Given the head of the first level of the list, 
flatten the list so that all the nodes appear in a single-level, doubly linked list.
Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.

Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.

Example 1:
https://assets.leetcode.com/uploads/2021/11/09/flatten11.jpg
Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
https://assets.leetcode.com/uploads/2021/11/09/flatten12.jpg
Explanation: The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:

Example 2:
https://assets.leetcode.com/uploads/2021/11/09/flatten2.1jpg
Input: head = [1,2,null,3]
Output: [1,3,2]
https://assets.leetcode.com/uploads/2021/11/24/list.jpg
Explanation: The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:

Example 3:

Input: head = []
Output: [] '''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        if head:
            n_stack = []        
            curr_node = head
            while curr_node:
                if curr_node.next:						
                    # Push the "next" (if there's a "next") first.
                    n_stack.append(curr_node.next)
                if curr_node.child:						
                    # Then push the "child" (if there's a child), 
                    n_stack.append(curr_node.child)		
                    # so that the "stack" would pop the immediate "child" 
                    curr_node.child = None 				
                    # before any previous encountered "next".
                if n_stack:								
                    # It will "recurse" down and bubble back up eventually.
                    next_node = n_stack.pop()			
                    # Unless it has traversed through all the nodes,
                    curr_node.next = next_node          
                    # there's always some node left in the stack to pop.     
                    next_node.prev = curr_node 			
                    # Simply link up with whatever comes from the stack.
                curr_node = curr_node.next 				
                # To the next node, or None if there's no more
        return head
