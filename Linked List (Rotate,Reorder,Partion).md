# Rotate a list

**Brute force- put last node and put it  infront of head for k time- O(N*K)**

**Approach-2 find length then move the current length-k times ahead.... Now make the head be current->next and make current->next be NULL**

https://leetcode.com/problems/rotate-list/

```
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
          if(!head || !head->next || k==0) return head;
            
        ListNode* curr=head;
        int len=1;
        while(curr->next)
        {
            curr=curr->next;
            len++;
        }
       
        curr->next=head;
        
        k=k%len;
        k=len-k;
        
        while(k--)
        {
            curr=curr->next;
        }
        
        head=curr->next;
        curr->next=NULL;
        
        return head;
    }
};
```
