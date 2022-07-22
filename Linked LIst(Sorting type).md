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
