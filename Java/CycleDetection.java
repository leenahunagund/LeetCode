/*A linked list is said to contain a cycle if any node is visited more than once while traversing the list.
Given a pointer to the head of a linked list, determine if it contains a cycle. If it does, return . Otherwise, return .

Input Format

The code stub reads from stdin and passes the appropriate argument to your function.
The custom test cases format will not be described for this question due to its complexity. 
Expand the section for the main function and review the code if you would like to figure out how to create a custom case.*/
static boolean hasCycle(SinglyLinkedListNode head) {
        if(head==null) return false;
        SinglyLinkedListNode fp=head;
        SinglyLinkedListNode sp=head;
        while(fp!=null && fp.next!=null){
            fp=fp.next.next;
            sp=sp.next;
            if (fp==sp) return true;
        }
        return false;
    }
