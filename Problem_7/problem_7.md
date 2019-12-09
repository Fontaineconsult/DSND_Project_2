In problem 7 we use a Trie to implement an HTTP router data structure. The solution only requires a Trie and no
other algorithm or data structure. When a route is provided to the Trie we split the "/" and store each section
of the path as a node. 

When we need to lookup a if a path is valid we simply walk the Trie based on the provided path. If no path is found
we get a 404.

Walking the Trie is O(N) where N is the length of the path.


