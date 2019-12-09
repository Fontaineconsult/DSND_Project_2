In problem 5 we use a Trie and recursion to build an auto complete lookup data structure.

The Trie stores our word-bank. When a string is provided to the trie, we loop the input string and follow the trie.
If we reach the end of the string and find that it is a word, we return it. If we reach 
the end of the string and we don't have a word, we recurse in the remainder of entire Trie and return the
suffixes as a list. If we encounter a character in the search string that isn't in the Trie, we return False, 
we know there is no word that can match.


Big O of the find method depends on the size of the Trie (how many words are stored). Walking a Trie is O(N),
where N is the size of the input string. Recursing the trie is O(M), where M is the number of remaining paths
in the Trie after we have reached the end of our input string as we must walk the entire remainder of the Trie.

We can say Trie walking is O(N) 

