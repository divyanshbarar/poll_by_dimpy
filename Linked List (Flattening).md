## Flattening a linked List

https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1

**Merging from last two list to the front**

```
 Node* mergeTwoSortedList(Node* first,Node* second)
    {
        if(first == NULL)
            return second;
            
        if(second == NULL)
            return first;
            
        if(first -> data < second -> data)
        {
            first -> bottom = mergeTwoSortedList(first -> bottom, second);
            return first;
        }
        else
        {
            second -> bottom = mergeTwoSortedList(first, second -> bottom);
            return second;
        }
    }
Node *flatten(Node *root)
{
//   Base Case 
    if(root == NULL || root -> next == NULL)
    {
        return root;
    }
    
    Node* down = root;
    Node* right = flatten(root -> next);
    
    return mergeTwoSortedList(down,right);
}
```

## Flattening a multilevel linked list

https://youtu.be/kvCYxPKpPGg 

**Approach1- using a queue**

**Approach2- using tail pointer**

https://www.geeksforgeeks.org/flatten-a-linked-list-with-next-and-child-pointers/

```
void flattenList(Node *head)
{
    /*Base case*/
    if (head == NULL)
    return;
 
    Node *tmp;
 
    /* Find tail node of first level linked list */
    Node *tail = head;
    while (tail->next != NULL)
        tail = tail->next;
 
    // One by one traverse through all nodes of first level
    // linked list till we reach the tail node
    Node *cur = head;
    while (cur != tail)
    {
        // If current node has a child
        if (cur->child)
        {
            // then append the child at the end of current list
            tail->next = cur->child;
 
            // and update the tail to new last node
            tmp = cur->child;
            while (tmp->next)
                tmp = tmp->next;
            tail = tmp;
        }
 
        // Change current node
        cur = cur->next;
    }
    
  ```
  
  ## Flattening a multilevel Doubly Linked List
  
  https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
  
  ```
  class Solution {
public:
    Node* flatten(Node* head) {
        
        if(!head)
            return head;
        
        Node* curr=head;
        
        while(curr)
        {
            if(curr->child==NULL)
            {
                curr=curr->next;
                continue;
            }
            
            Node *temp=curr->child;
            
            while(temp->next)
            {
                temp=temp->next;
            }
            
            temp->next=curr->next;
            
            if(curr->next!=NULL)
                curr->next->prev=temp;
            
            curr->next=curr->child;
            curr->next->prev=curr;
            curr->child=NULL;
        }
        
        return head;
    }
};
```
  
