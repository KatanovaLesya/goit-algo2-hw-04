from longest_common import LongestCommonWord

def run_tests():
    trie = LongestCommonWord()
    assert trie.find_longest_common_word(["flower", "flow", "flight"]) == "fl"

    trie = LongestCommonWord()
    assert trie.find_longest_common_word(["interspecies", "interstellar", "interstate"]) == "inters"

    trie = LongestCommonWord()
    assert trie.find_longest_common_word(["dog", "racecar", "car"]) == ""

    trie = LongestCommonWord()
    assert trie.find_longest_common_word([]) == ""

    print("Усі тести пройдено успішно")

if __name__ == "__main__":
    run_tests()
