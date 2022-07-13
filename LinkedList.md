**Reverse a Linked List**
https://leetcode.com/problems/reverse-linked-list/
```
class Solution {
public:

    ListNode* reverseList(ListNode* head) {

         ListNode *prev=NULL, *curr=head;
        while(curr!=NULL)
        {
            ListNode *forward=curr->next; 
            curr->next=prev;
            prev=curr;
            curr=forward;
        }
        return prev;
        
    }
};
```
**Reverse a Linked List 2**
https://leetcode.com/problems/reverse-linked-list-ii/
```
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        
        if(head==NULL)
            return head;
        
        ListNode *prev=NULL;
        ListNode* curr=head;
        
        while(left>1)   // have to start with position of left 1 (think of 1-based Indexing)
        {
            prev=curr;
            curr=curr->next;
           left--;
            right--;
        }
        //Now Curr will be at starting point
        ListNode * start=prev, *tail=curr;
        
        ListNode* forward=NULL;
        while(right>0) //start reversing
        {
            forward=curr->next;
            curr->next=prev;
            prev=curr;
            curr=forward;
            right--;
        }
		// By this time the between list is reversed
		
        tail->next=curr;//pointing right
        
        if(start!=NULL) //pointing left
             start->next=prev;
        else
            head=prev;
        return head;
    }
};
```
**Reverse a Doubly lInked List**
https://www.geeksforgeeks.org/reverse-a-doubly-linked-list/
```
Node* reverseDLL(Node * head)
{
    //Your code here
          Node* prev = NULL;
    Node* curr = head;
    Node* temp;
    
    while(curr){
        temp = curr->next;
        curr->next = prev;
        curr->prev = temp;
        prev = curr;
        curr = temp;
    }
    
    return prev;
}
```
**Reverse Nodes in K-groups**
https://leetcode.com/problems/reverse-nodes-in-k-group/
```
class Solution {
public:
    ListNode* reverse(ListNode* head, ListNode* tail) {
        ListNode* current = head;
        ListNode *prev = NULL, *next = NULL;
 
        while (current != tail) {
            next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        }
        
        return prev;
    }
    ListNode* reverseKGroup(ListNode* head, int k) {
        
       ListNode* ptr=head;
        
        for(int i=0;i<k;i++)
        {
            if(!ptr) return head;
            ptr=ptr->next;
        }
        
        ListNode* tmp=reverse(head,ptr);
        
        head->next=reverseKGroup(ptr,k);
        
        return tmp;
    }
};
```

**Reverse Nodes in K-group**
https://leetcode.com/problems/reverse-nodes-in-k-group/
```
class Solution {
public:
    ListNode* reverse(ListNode* head, ListNode* tail) {
        ListNode* current = head;
        ListNode *prev = NULL, *next = NULL;
 
        while (current != tail) {
            next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        }
        
        return prev;
    }
    ListNode* reverseKGroup(ListNode* head, int k) {
        
       ListNode* ptr=head;
        
        for(int i=0;i<k;i++)
        {
            if(!ptr) return head;
            ptr=ptr->next;
        }
        
        ListNode* tmp=reverse(head,ptr);
        
        head->next=reverseKGroup(ptr,k);
        
        return tmp;
    }
};
```

**Middle Of Linked List**
https://leetcode.com/problems/middle-of-the-linked-list/
```
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        
        ListNode* noob=head, *pro=head->next;
        
        while(pro!=NULL)
        {
            pro=pro->next;
            if(pro!=NULL)
                pro=pro->next;
            
            noob=noob->next;
        }
        
        return noob;
    }
};
```

