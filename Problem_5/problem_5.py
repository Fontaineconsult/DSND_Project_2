class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

    def insert(self, char):
        self.children[char] = TrieNode()

    def suffixes(self):

        suffixes = []
        for key, value in self.children.items():

            suffixes = self._recurse_trie(value , key)

        return suffixes

    def _recurse_trie(self, node, key, suffix='', suffixes=[]):

        suffix += key

        if node.is_word:
            suffixes.append(suffix)

        for key, value in node.children.items():

            self._recurse_trie(value, key, suffix, suffixes)

        return suffixes

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, trie):

        current_node = self.root

        for char in trie:
            if char not in current_node.children:
                current_node.insert(char)
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):

        current_node = self.root
        word = ''

        for char in prefix:
            if char in current_node.children:

                current_node = current_node.children[char]
                word += char

            elif char not in current_node.children:

                return False
        if current_node.is_word:

            return word
        else:
            return current_node.suffixes()

    def walk_trie(self):

        current_node = self.root
        self._recurse_walk(current_node)

    def _recurse_walk(self, node):
        for char in node.children.keys():
            if node.is_word:

                return True
            self._recurse_walk(node.children[char])
            return False


MyTrie = Trie()

wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory", "facticity", "factual",
    "trie", "trigger", "triggered", "trigonometry", "tripod", "trinity", "trinidad", "tricorder", "trinket", "triforce"
]


for word in wordList:
    MyTrie.insert(word)


print(MyTrie.find("facticity"))
print(MyTrie.find("tri"))
print(MyTrie.find("fluffy"))