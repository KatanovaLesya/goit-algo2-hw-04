from trie import Trie

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
            raise ValueError("Очікується список рядків")

        if not strings:
            return ""

    
        for i, word in enumerate(strings):
            self.put(word, i)

    
        node = self.root
        prefix = ""
        while True:
            if len(node.children) != 1 or node.is_end:
                break
            char = next(iter(node.children))
            prefix += char
            node = node.children[char]

        return prefix
