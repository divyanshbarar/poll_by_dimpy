# Binary Search

```
class Solution {
public:
    int search(vector<int>& nums, int target) {
     
        int l=0,r=nums.size()-1;
        
        while(l<=r)
        {
            int mid=l+(r-l)/2;    //avoid overflow
            cout<<nums[mid]<<endl; 
            if(nums[mid]==target)
                return mid;
            else if(nums[mid]<target)
                {
                    l=mid+1;
                }
            else  if(nums[mid]>target)
                    r=mid-1;
        }
            
        return -1;
    }
};
```

# First Position in Sorted array

```
int start=0,end=n-1;
        int fo=-1;
        while(start<=end)
        {
            int mid=start+((end-start)/2);
           
            if(nums[mid]==target)
            {  fo=mid;
             end=mid-1;
            }
            else if(nums[mid]<target)
                start=mid+1;
            else
                end=mid-1;
        }
         return fo;
  ```
  
# Last position in Sorted array
  
  ```
  start=0,end=n-1;
        int lo=-1;
        while(start<=end)
        {
            int mid=start+((end-start)/2);
           
            if(nums[mid]==target)
            {  lo=mid;
              start=mid+1;
            }
            else if(nums[mid]<target)
                start=mid+1;
            else
                end=mid-1;
        }
        return lo;
  ```
    
      
  # Find the number of occurrences of an element in a sorted array
  
  **logic= last_Occur-first_Occur + 1** 
  ```
   int n = nums.size();
    int first = firstOcc(nums, target,n);
    int second = lastOcc(nums,target, n);
   int occur = second-first+1;
    return occur ;
   ```
   
   **One line code To impress**
  
  ```
   return upper_bound(A.begin(),A.end(),K)-lower_bound(A.begin(),A.end(),K); //O(log(n))
   
   ```
