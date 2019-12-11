The rotated binary search algorithm is actually two different binary searches
combined together. 

To do a binary search in a rotated array we need to first find the "pivot" point.
In an ascending numeric sequence the pivot will always be less than the preceding 
value. 

To efficiently find the pivot point, we start by comparing the middle value
of the array to the end value of the array. If the end value is lower, we know the
pivot is to the right, and vice versa. We then shift our compare point
either direction until we find the pivot.

Once we have the pivot we can run the binary search on the right or left of the 
pivot depending on whether the search value is within that side.


Complexity is O(log n) as binary search is log N as each search searches
half the original amount.

Space complexity is O(M) where M is the size of the rotated array.

