# how many times an array should be rotated to be in sorted form

**Mnimum No. Index will be the no. of time rotation**

# Find Minimum in Rotated Sorted Array
  ---> doesnt contains duplicates
  
  **logic => if prev is bigger than current it means current is minimum**
  ```
          int n=nums.size();
      
        int start=0,end=n-1;
        while(start<=end)
        {
           if (nums[start]<=nums[end])
            return nums[start];
            
            int mid=start+((end-start)/2);
            int prev=(mid+n-1)%n;
          
            if(nums[prev]>nums[mid])
                return nums[mid];
            else if(nums[start]<=nums[mid])
                start=mid+1;
            else 
                end=mid-1;
        }
        
        return 0;
  ```
# Find Minimum in Rotated Sorted Array 2
  --> contains duplicates
  
  **logic => lowering the upper bound**
  ```
   int findMin(vector<int>& nums) {
          
        int n=nums.size();
      
        int start=0,end=n-1;
        while(start<end)
        {
 
            int mid=start+((end-start)/2);
            if(nums[end]<nums[mid])
                start=mid+1;
            else if(nums[end]>nums[mid])
                end=mid;
            else 
                end--;
        }
        cout<<start<<endl;
        return nums[start];
    }
  ```
    
 # Search in Rotated Sorted Array
 
 **Two approaches => 1) Find minimum and bs for left half and bs for right half** -> wont work for containing duplicates
 
 **2)is monotonic then move the start pointer ahead**
 
```
int beg=0,end=nums.size()-1,mid;
        while(beg<=end)
        {
            mid=(beg+end)/2;
            if(nums[mid]==target)
                return mid;
            // if till this the array is monotonic increasing
            if(nums[beg]<=nums[mid])
            {
                if(target<=nums[mid] && target>=nums[beg])
                    end=mid-1;
                else
                    beg=mid+1;
            }
            
            else // if not monotonic in nature
            {
                if(target>=nums[mid] && target<=nums[end])
                   beg=mid+1;
                else
                    end=mid-1;
            }
            
        }
        return -1;
        
 ```
     
# Search in Rotated Sorted Array 2 (Containing duplicates)

```
 bool search(vector<int>& nums, int target) {
        
           int beg=0,end=nums.size()-1,mid;
        while(beg<=end)
        {
            mid=(beg+end)/2;
            if(nums[mid]==target)
                return true;
            if( (nums[beg] == nums[mid]) && (nums[end] == nums[mid]) ) {++beg; --end;}
            else if(nums[beg]<=nums[mid])
            {
                if(target<=nums[mid] && target>=nums[beg])
                    end=mid-1;
                else
                    beg=mid+1;
            }
            
            else
            {
                if(target>=nums[mid] && target<=nums[end])
                   beg=mid+1;
                else
                    end=mid-1;
            }
            
        }
        return false;
        
    }
```
