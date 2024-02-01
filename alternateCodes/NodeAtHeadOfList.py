'''Given a pointer to the head of a linked list, 
insert a new node before the head. The  value in the new node should point to  and the  value should be replaced with a given value.
Return a reference to the new head of the list. The head pointer given may be null meaning that the initial list is empty.

Sample Input
5
383
484
392
975
321

Sample Output
321
975
392
484
383

Explanation
Intially the list in NULL. After inserting 383, the list is 383 -> NULL.
After inserting 484, the list is 484 -> 383 -> NULL.
After inserting 392, the list is 392 -> 484 -> 383 -> NULL.
After inserting 975, the list is 975 -> 392 -> 484 -> 383 -> NULL.
After inserting 321, the list is 321 -> 975 -> 392 -> 484 -> 383 -> NULL.'''

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
# my code, ran all 6 testcases
def insertNodeAtHead(llist, data):
    # Write your code here
    newnode=SinglyLinkedListNode(data)
    if llist is None:
        llist=newnode
    else:
        newnode.next=llist
        llist=newnode
    return llist

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head
    
    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')
    
    fptr.close()
