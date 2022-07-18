**Remove Linked List Elemnets**

https://leetcode.com/problems/remove-linked-list-elements/

```
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        if(head==NULL)
            return head;
        
        while(head!=nullptr && head->val==val){     // this piece of code to handle same key at head
                                                    // ex- [7,7,7,7]
            head = head->next;
        }
        ListNode* prev=NULL,*curr=head;
     
        while(curr!=NULL)
        {
            if(curr->val==val)
            {
                prev->next=curr->next;
                curr=curr->next;
                
            }
            else
            {
                prev=curr;
                curr=curr->next;
            }
        
        }
        
        return head;
    }
};
```
![list2](https://user-images.githubusercontent.com/68277579/179561826-b55129a0-9bca-418d-a482-3c08499a7217.jpg)

**Remove Duplicates from Sorted list**

https://leetcode.com/problems/remove-duplicates-from-sorted-list/

```
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head) return NULL;
        if (!head->next) return head;
        
        ListNode* curr=head;
        
        while(curr!=NULL)
        {
            while((curr->next!=NULL) && curr->val==curr->next->val)
            {
                curr->next=curr->next->next;
            
            }
            
                curr=curr->next;
        
        }
        
        return head;
    }
};
```
**Remove duplicates from Sorted List 2**

https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
![linkedlist1](https://user-images.githubusercontent.com/68277579/179563614-7d6cd47e-e9d2-4ab9-ae36-b2e1e2c3bcf5.jpg)

```
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head) return 0;
        if (!head->next) return head;
        
        ListNode* curr=head;
        ListNode* prev=NULL;
        
        while(curr!=NULL)
        {
            if((curr->next!=NULL) && curr->val==curr->next->val)
            {
                 while((curr->next!=NULL) && curr->val==curr->next->val)
                    {
                        curr->next=curr->next->next;

                    }
                if(!prev) // This condition means element at the head is repeat So, head pointer needs to be  shifted.
                    head=curr->next;
                else
                    prev->next=curr->next;
            }
           else
               prev=curr;
            curr=curr->next;
           
        }
        return head;
    }
};
```
**Remove Duplicates frfom Unsorted**

I/P- 12->3->4->12->5->4->6
O/P- 12->3->4->5->6
https://www.geeksforgeeks.org/remove-duplicates-from-an-unsorted-linked-list/

```
void removeDuplicates(struct Node* start)
{
    // Hash to store seen values
    unordered_set<int> seen;
 
    /* Pick elements one by one */
    struct Node* curr = start;
    struct Node* prev = NULL;
    while (curr != NULL) {
        // If current value is seen before
        if (seen.find(curr->data) != seen.end()) {
            prev->next = curr->next;
            delete (curr);
        }
        else {
            seen.insert(curr->data);
            prev = curr;
        }
        curr = prev->next;
    }
}
```
**REMOVE cycle**

https://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list/
```
void removeLoop(Node* head)
    {
        Node *fast = head,*slow = head,*hold=head;
        while(fast && fast->next){
            fast = fast->next->next;
            slow = slow->next;
            if(slow == fast){
                while(slow != hold){
                    hold=hold->next;
                    slow=slow->next;
                }
                while(fast->next!=slow)fast=fast->next;
                fast->next = NULL;
            }
        }
    }
 ```
