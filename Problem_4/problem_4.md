This implementation of the DNFP splits an array into three groups by tracking two pivot points ("mid", "end") that
delineate the separation between the three groups (0,1,2). As we iterate through the list we compare the current
value with our current mid value (which starts at index 0).
 
If the current value is less than the mid value,
we move the current value to the start of the list and move the mid value index up. if the current value greater than the mid value, we move
the current value to the end of the list and move the end index down. And if the current value is equal to the mid value, we leave it where
it is. 

This operation only requires a single traversal of the list. Therefore this algorithm has is O(N). Where N is the size of the list.
Space complexity is O(N) for the size of the input list.


