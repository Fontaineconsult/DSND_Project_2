In problem 5 we use a Trie and recursion to build an auto complete lookup data structure.

To lookup a word and its suffixes we provide a string to our Trie. The .find method walks the prefix trie for 
each character in the string. When we reach the end of the string we return the Node object we are currently
visiting. The Node object provides a method to return all the remaining suffixes (if there are any). To
find the suffixes we recurse through the remainder of the Trie starting from the calling node. Each
time we find a complete word Node we append the suffix and return the list.

Big O of the find method depends on the size of the Trie (how many words are stored). Walking a Trie is O(N),
where N is the size of the input string. Recursing the trie is O(M), where M is the number of remaining paths
in the Trie after we have reached the end of our input string as we must walk the entire remainder of the Trie.

We can say Trie walking is O(N)
Space complexity is O(M) where M is the number of nodes. The number of nodes is determined by
the number of unique prefixes in our wordbank.

