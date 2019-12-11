class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

    def insert(self, char):
        self.children[char] = TrieNode()

    def suffixes(self):

        suffixes = []

        for key, value in self.children.items():

            suffixes = self._recurse_trie(value, key, '', suffixes)

        return suffixes

    def _recurse_trie(self, node, key, suffix, suffixes):

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

        if prefix == "":
            return None

        for char in prefix:
            if char in current_node.children:

                current_node = current_node.children[char]
                word += char

            elif char not in current_node.children:
                return None

        if current_node.is_word:

            return current_node
        else:
            return current_node

    def walk_trie(self):

        current_node = self.root
        self._recurse_walk(current_node)

    def _recurse_walk(self, node):
        for char in node.children.keys():
            if node.is_word:
                return True
            self._recurse_walk(node.children[char])
            return None


MyTrie = Trie()

wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory", "facticity", "factual",
    "trie", "trigger", "triggered", "trigonometry", "tripod", "trinity", "trinidad", "tricorder", "trinket", "triforce"
]


for word in wordList:
    MyTrie.insert(word)


ant = MyTrie.find("ant")
print(ant.suffixes(), ant.is_word)

an = MyTrie.find("an")
print(an.suffixes(), an.is_word)

facticity = MyTrie.find("facticity")
print(facticity.suffixes(), facticity.is_word)

tri = MyTrie.find("tri")
print(tri.suffixes(), tri.is_word)


fluffy = MyTrie.find("fluffy")
if fluffy:
    print(fluffy.suffixes(), fluffy.is_word)
else:
    print(fluffy)

empty = MyTrie.find("")
if empty:
    print(empty.suffixes(), empty.is_word)
else:
    print(empty)

