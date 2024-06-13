class TrieNode:

    def __init__(self):
        self.children = [None]*26
        self.isleaf = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.isleaf = True

    def search(self, word: str) -> bool:
        curr = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return curr.isleaf and curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for letter in prefix:
            index = ord(letter) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return True

    def deleteKey(self, root, key):
        # unsure
        n = len(key)
        for i in range(n):
            index = ord(key[i])-ord('a')
            if root.children[index]:
                root = root.children[index]
            else:
                return
        root.isleaf = False

