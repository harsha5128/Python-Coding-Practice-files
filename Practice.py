from collections import deque, defaultdict
from typing import List

def findLadders(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    word_set = set(wordList)
    if endWord not in word_set:
        return []

    # Initialize BFS variables
    level = {beginWord: 0}
    parents = defaultdict(list)
    queue = deque([beginWord])
    word_len = len(beginWord)
    found_end = False
    current_level = 0

    while queue and not found_end:
        current_level += 1
        # Process all nodes at the current level
        for _ in range(len(queue)):
            word = queue.popleft()
            for i in range(word_len):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == word[i]:
                        continue
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in word_set:
                        if next_word not in level:
                            level[next_word] = current_level
                            queue.append(next_word)
                            parents[next_word].append(word)
                            if next_word == endWord:
                                found_end = True
                        elif level[next_word] == current_level:
                            parents[next_word].append(word)
                            if next_word == endWord:
                                found_end = True

    if not found_end:
        return []

    # Backtrack to build paths
    res = []
    path = [endWord]

    def backtrack(word):
        if word == beginWord:
            res.append(path[::-1])
            return
        for parent in parents[word]:
            path.append(parent)
            backtrack(parent)
            path.pop()

    backtrack(endWord)
    return res

# Example test cases
if __name__ == "__main__":
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot","dot","dog","lot","log","cog"]
    print(findLadders(beginWord1, endWord1, wordList1))
    # Expected Output:
    # [
    #   ["hit","hot","dot","dog","cog"],
    #   ["hit","hot","lot","log","cog"]
    # ]

    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot","dot","dog","lot","log"]
    print(findLadders(beginWord2, endWord2, wordList2))
    # Expected Output: []

    beginWord3 = "a"
    endWord3 = "c"
    wordList3 = ["a","b","c"]
    print(findLadders(beginWord3, endWord3, wordList3))
    # Expected Output:
    # [
    #   ["a","c"]
    # ]
