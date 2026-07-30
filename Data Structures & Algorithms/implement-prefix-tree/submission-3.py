class TrieNode:
    def __init__(self, val=None, is_end=False):
        self.val = val
        self.children = {}
        self.is_end = is_end

class PrefixTree:
    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.head
        # structure is {character : -> {a:, b:{}, c: {}}

        for i in range(len(word)):
            c = word[i]
            if c not in curr.children:
                curr.children[c] = TrieNode(c)
            curr = curr.children[c]
        curr.is_end = True
                
    def search(self, word: str) -> bool:
        # What is the bottom out condtion
        # "" -> d -> o -> g has no children
        curr = self.head
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        
        