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

# Reorder a Linked List

https://leetcode.com/problems/reorder-list/

**Cut it half... reverse the Second one... merge both list**

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
    
    void merge(ListNode* l1,ListNode* l2)
    {
        while(l1)
        {
        ListNode* l1_next=l1->next;
        ListNode* l2_next=l2->next;
            
            l1->next=l2;
            
            if(!l1_next)
                break;
            
            l2->next=l1_next;
            l1=l1_next;
            l2=l2_next;
        }
    }
    void reorderList(ListNode* head) {
         if(head==NULL ||!head->next)
            return ;
         ListNode* noob=head, *pro=head->next;
        ListNode* temp=NULL;
        while(pro!=NULL)
        {
            pro=pro->next;
            if(pro!=NULL)
                pro=pro->next;
             temp=noob;
            noob=noob->next;
           
        }
        
        temp->next=NULL;
        
        noob=reverseList(noob);
        
        merge(head,noob);
    }
};
```

# odd even Linked list

**We put one odd as head and even as head->next Now start adding odd to odd and even to even**

https://leetcode.com/problems/odd-even-linked-list/

```
class Solution {
public:
  
    ListNode* oddEvenList(ListNode* head) {
        if(!head)
            return head;
        
        ListNode *odd=head,*even=head->next,*even_head=even;
        
        while(even && even->next)
        {
            odd->next=even->next;
            odd=odd->next;
            
            even->next=odd->next;
            even=even->next;
        }
        
        odd->next=even_head;
        
        return head;
    }
};
```
