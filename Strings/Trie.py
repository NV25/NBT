class TrieNode(object):
    def __init__(self, c):
        self.char = c
        self.children = {}
        self.isWord = False

class PrefixTrie(object):
    def __init__(self):
        self.root = TrieNode(0)

    def insertWord(self, word):
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                newNode = TrieNode(c)
                cur.children[c] = newNode
                cur = cur.children[c]

        cur.isWord = True

    def startsWith(self, prefix):
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False

            cur = cur.children[c]

        return cur.isWord

