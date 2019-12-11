In problem 7 we use a prefix trie to implement an HTTP router data structure. The prefix trie is an
ideal data structure for this task because the prefix trie does not duplicate the similar parts of 
slightly different strings (the prefix). Lookup in a prefix trie is usually O(M) where M is the length
of the path traveled. 
 
 The solution only requires a Trie and no
other algorithm or data structure. When a route is provided to the Trie we split the "/" and store each section
of the path as a node. 

When we need to lookup a if a path is valid we simply walk the Trie based on the provided path. If no path is found
we get a 404.

Walking the Trie is O(M) where M is the length of the path.
Space complexity is O(NM) where N is the number of nodes and M is the length string name (path component) in the node. 


