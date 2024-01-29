'''Complete the printLinkedList function in the editor below.
printLinkedList has the following parameter(s):
SinglyLinkedListNode head: a reference to the head of the list
For each node, print its  value on a new line.

Input Format
The first line of input contains , the number of elements in the linked list.
The next  lines contain one element each, the  values for each node.

Note: Do not read any input from stdin/console. Complete the printLinkedList function in the editor below

Sample Input
2
16
13

Sample Output
16
13

Explanation
There are two elements in the linked list. They are represented as 16 -> 13 -> NULL. So, the printLinkedList function should print 16 and 13 each on a new line.'''

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

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#my code , passed all 8 test cases
def printLinkedList(head):
    while (head.next)!=None:
        print(head.data)
        head=head.next
    print(head.data)

if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    printLinkedList(llist.head)
