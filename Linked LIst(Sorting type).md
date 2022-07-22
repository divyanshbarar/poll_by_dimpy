## Sort 0 1 2

**data replacement not allowed**

https://www.geeksforgeeks.org/sort-linked-list-0s-1s-2s-changing-links/

```
Node* sortList(Node* head)
{
    if (!head || !(head->next))
        return head;
 
    // Create three dummy nodes to point to beginning of
    // three linked lists. These dummy nodes are created to
    // avoid many null checks.
    Node* zeroD = newNode(0);
    Node* oneD = newNode(0);
    Node* twoD = newNode(0);
 
    // Initialize current pointers for three
    // lists and whole list.
    Node *zero = zeroD, *one = oneD, *two = twoD;
 
    // Traverse list
    Node* curr = head;
    while (curr) {
        if (curr->data == 0) {
            zero->next = curr;
            zero = zero->next;
        }
        else if (curr->data == 1) {
            one->next = curr;
            one = one->next;
        }
        else {
            two->next = curr;
            two = two->next;
        }
        curr = curr->next;
    }
 
    // Attach three lists
    zero->next = (oneD->next) ? (oneD->next) : (twoD->next);
    one->next = twoD->next;
    two->next = NULL;
 
    // Updated head
    head = zeroD->next;
 
    // Delete dummy nodes
    delete zeroD;
    delete oneD;
    delete twoD;
 
    return head;
}
```

## Merge Two Sorted List

https://leetcode.com/problems/merge-two-sorted-lists/

```
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
          ListNode dummy(INT_MIN);
        ListNode *tail = &dummy;
        
        while (l1 && l2) {
            if (l1->val < l2->val) {
                tail->next = l1;
                l1 = l1->next;
            } else {
                tail->next = l2;
                l2 = l2->next;
            }
            tail = tail->next;
        }

        tail->next = l1 ? l1 : l2;
        return dummy.next;
    }
};
```

## Merge K Sorted List

https://leetcode.com/problems/merge-k-sorted-lists/

**Refer Copy for approach1 and 2 and This algo uses min-heap**

```
class mycompare{
	public:
	bool operator()(const ListNode* a,const ListNode* b)
    {
        return (a->val>b->val);
    }
        };
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
         ListNode *dummy=new ListNode(0);
        ListNode *tail=dummy;
        priority_queue<ListNode*,vector<ListNode*>,mycompare> pq;
        for(int i=0;i<lists.size();i++)
        {
            if(lists[i]!=NULL)
                pq.push(lists[i]);
        }
        
        while(!pq.empty())
        {
            auto temp=pq.top();
            pq.pop();
            tail->next=temp;
            tail=tail->next;
            if(temp->next)
                pq.push(temp->next);
        }
        return dummy->next;
    }
};
```

## Merge Sort Linked List

https://leetcode.com/problems/sort-list/

**Divide the array In two parts then apply Merge 2 sorted list**

**Time Complexity-O(nlogn)**

```
class Solution {
public:
    ListNode* sortList(ListNode* head) {
        
        if (head == NULL || head->next == NULL)
            return head;
        
        //finding mid
        ListNode* slow = head;
        ListNode* fast = head->next;
        
        while (fast != NULL && fast->next != NULL)
        {
            slow = slow->next;
            fast = fast->next->next;
        }
        //divide the list into two parts 
        fast = slow->next;
        slow->next = NULL;
        
        return merge(sortList(head), sortList(fast));
    }
    
    ListNode* merge(ListNode* l1, ListNode* l2)
    {
        ListNode dump(0);
        ListNode* cur = &dump;
        
        while (l1 != NULL && l2 != NULL)
        {
            if (l1->val < l2->val)
            {
                cur->next = l1;
                l1 = l1->next;
            }
            else
            {
                cur->next = l2;
                l2 = l2->next;
            }
                
            cur = cur->next;
        }
        
        if (l1 != NULL)
            cur->next = l1;
        else
            cur->next = l2;
            
        return dump.next;
    }
};
```

## Insertion Sort

https://leetcode.com/problems/insertion-sort-list/

```
class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
        ListNode * dummy=new ListNode(-1,head);
        ListNode *prev=head;
        ListNode * curr=head->next;
        
        while(curr!=NULL)
        {
            if(prev->val>curr->val)
            {
                ListNode* temp=dummy;
                
                while(curr->val>temp->next->val)
                {
                    temp=temp->next;
                }
                
                prev->next=curr->next;
                curr->next=temp->next;
                temp->next=curr;
                curr=prev->next;
                
            }
            else
            {
                prev=curr;
                curr=curr->next;
            }
        }
        
        return dummy->next;
    }
};
```

