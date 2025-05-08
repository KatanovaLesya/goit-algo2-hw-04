class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def put(self, word, value):
        if not isinstance(word, str):
            raise ValueError("Слово має бути рядком")

        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.value = value

    def get(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        if node.is_end:
            return node.value
        return None

    def words(self):
        result = []

        def dfs(node, prefix):
            if node.is_end:
                result.append(prefix)
            for char, child in node.children.items():
                dfs(child, prefix + char)

        dfs(self.root, "")
        return result
