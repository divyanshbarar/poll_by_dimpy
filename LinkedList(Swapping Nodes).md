## Swapping Nodes In Linked list kth from beginning and kth from end 

https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

```
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
      ListNode* prev=head,*curr=head;
        
        while(k>1)
        {
            
            curr=curr->next;
            k--;
        }
       
        ListNode *kNode=curr;
        
        while(curr->next!=NULL)
        {
            prev=prev->next;
            curr=curr->next;
        }
        
        int val=kNode->val;
        kNode->val=prev->val;
        prev->val=val;
        
        return head;
    }
};
```

## Swap Nodes in Pairs

https://leetcode.com/problems/swap-nodes-in-pairs/

```
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
   
     if(!head || !head->next) return head; //If there are less than 2 nodes in the given nodes, then no need to do anything just return the list as it is.
		
        ListNode* dummyNode = new ListNode(0,head);
        
        ListNode* prevNode=dummyNode;
        ListNode* currNode=head;
        
        while(currNode && currNode->next){
            prevNode->next = currNode->next;
            currNode->next = prevNode->next->next;
            prevNode->next->next = currNode;
            
            prevNode = currNode;
            currNode = currNode->next;
        }
        
        return dummyNode->next;
    } 
    
};
```
