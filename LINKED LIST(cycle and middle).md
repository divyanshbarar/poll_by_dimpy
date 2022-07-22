**IS circular or not**
https://practice.geeksforgeeks.org/problems/circular-linked-list/1
```
bool isCircularList(Node *head){
   if(head == NULL)
      return true;
   Node *node = head->next;
   while(node != NULL && node != head){
      node = node->next;
   }
   if(node == head)
      return true;
      
   return false;
}
```

**Middle Of Linked List**
https://leetcode.com/problems/middle-of-the-linked-list/
```
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        
        ListNode* pro=head, *noob=head->next;
        
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

**Is palindrome Linked List**

https://leetcode.com/problems/palindrome-linked-list/

## slow=fast=head for middle
## reverse from mid to end
## traverse to th end

```
class Solution {
public:
     ListNode* middleNode(ListNode* head) {
        
        ListNode* noob=head, *pro=head;
        
        while(pro!=NULL)
        {
            pro=pro->next;
            if(pro!=NULL)
                pro=pro->next;
            
            noob=noob->next;
        }
        
        return noob;
     }
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
    bool isPalindrome(ListNode* head) {
        
        if(head==NULL)
            return true;
        
        
        ListNode* mid=middleNode(head);
        ListNode* last=reverseList(mid);
        
        ListNode* curr=head;
        while(last!=NULL)
        {
            if(curr->val!=last->val)
                return false;
            
            curr=curr->next;
            last=last->next;
        }
       
        return true;
    }
};
```
**Cycle detection**

## Proof
# A+x*c+B=2(A+y*C+B)
https://leetcode.com/problems/linked-list-cycle/
```
class Solution {
public:
    bool hasCycle(ListNode *head) {
         if (!head) 
            return false;
        
        ListNode *slow = head, *fast = head;
        
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) 
                return true;
        }
        
        return false;
    }
};
```

**Node at where cycle begins**
https://leetcode.com/problems/linked-list-cycle-ii/

```
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
         if (!head) 
            return NULL;
        
        ListNode *slow = head, *fast = head;
        bool flag=false;
        
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) 
            {
                fast=head;
                while(slow!=fast)
                {
                    slow=slow->next;
                    fast=fast->next;
                }
                return slow;
            }
        }
        
        return NULL;
    }
};
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

