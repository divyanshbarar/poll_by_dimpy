## Add Two Number in reversed manner(very important)

**Can be asked by add 1 to LL**

https://leetcode.com/problems/add-two-numbers/

![addtwonumber1](https://user-images.githubusercontent.com/68277579/180616184-d6893adc-f782-4cf2-806a-a26d02f512ab.jpg)

**Intiution no. should be added from lright side only**

```
class Solution {

public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
   
        ListNode *ptr = new ListNode();     //new list;
        ListNode *temp = ptr;
        
        int c = 0;
		//traversing both list till one of the list not reaches NULL
        while (l1 != NULL ||  l2 != NULL || c)
        {
            int sum = 0;
			// if l1  is not null
			// add l1-> value to sum
            if(l1 != NULL)
            {
                sum += l1->val;
                l1 = l1 -> next;
            }
            
			// if l2  is not null
			// add l2-> value to sum
            if(l2 != NULL)
            {
                sum += l2->val;
                l2 = l2 -> next;
            }
            
			// add carry to sum
            sum += c;
			// carry is updated by sum/10 because for 18 , 
			// 18 / 10 is 1 which is the carry
            c = sum/10;
			// add sum% 10 to new node as it containg the sum
            ListNode *node = new ListNode(sum%10);
            temp -> next = node;
            temp = temp -> next;
        }
        return ptr -> next;
    }
};
```

## Add two no. in straaight way

https://practice.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1

```
class Solution
{
     Node* addTwoNumbers(Node* l1, Node* l2) {
   
        Node *ptr = new Node(0);     //new list;
        Node *temp = ptr;
        
        int c = 0;
		//traversing both list till one of the list not reaches NULL
        while (l1 != NULL ||  l2 != NULL || c)
        {
            int sum = 0;
			// if l1  is not null
			// add l1-> value to sum
            if(l1 != NULL)
            {
                sum += l1->data;
                l1 = l1->next;
            }
            
			// if l2  is not null
			// add l2-> value to sum
            if(l2 != NULL)
            {
                sum += l2->data;
                l2 = l2-> next;
            }
            
			// add carry to sum
            sum += c;
			// carry is updated by sum/10 because for 18 , 
			// 18 / 10 is 1 which is the carry
            c = sum/10;
			// add sum% 10 to new node as it containg the sum
            Node *node = new Node(sum%10);
            temp -> next = node;
            temp = temp -> next;
        }
        return ptr -> next;
    }
    Node* reverseList(Node* head) {

         Node *prev=NULL, *curr=head;
        while(curr!=NULL)
        {
            Node *forward=curr->next; 
            curr->next=prev;
            prev=curr;
            curr=forward;
        }
        return prev;
        
    }
    public:
    //Function to add two numbers represented by linked list.
    struct Node* addTwoLists(struct Node* first, struct Node* second)  //<---------------------------------main code
    { 
        // code here
        first=reverseList(first);
        second=reverseList(second);
        
        Node* temp=addTwoNumbers(first,second);
        temp=reverseList(temp);
        return temp;
    }
};
```

## Clone a linked list with random and next pointer

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

https://leetcode.com/problems/copy-list-with-random-pointer/

**Intiution- Store a deep copy of each Node in a map corresponding to roginal one
then start assiging the pointers of original one to deep copy as it it**

```
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        
        unordered_map<Node*, Node*> mp;
      
        Node* curr = head;
        while (curr) {
            mp[curr] =new Node(curr->val);
            curr = curr->next;
        }
        curr = head;
        while (curr) {
            mp[curr]->next = mp[curr->next];
            mp[curr]->random = mp[curr->random];       //<------------------Magic Code
            curr= curr->next;
        }
        return mp[head];
        
    }
};
```

## Intersection of Linked List

https://leetcode.com/problems/intersection-of-two-linked-lists/

![160_statement](https://user-images.githubusercontent.com/68277579/180623008-1d919001-f9de-4a35-8582-b15f9e7cda92.png)

**Here is the Intiution-for pointer a length is l1 for pointer b length is l2 when one of them reaches null the differnce will be covered by another pointer and hence we made those both pointer aligned**

https://youtu.be/u4FWXfgS8jw

```
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if(!headA || !headB)
            return NULL;
        
        ListNode* a=headA,*b=headB;
        
        while(a!=b)
        {
            a=a==NULL? headB:a->next;
            b=b==NULL? headA: b->next;
        }
        
        return a;
    }
};
```

