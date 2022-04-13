from typing import List, Set
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
    
        # have to define a sub function because we can't hash a mutable list for memoization
        @lru_cache
        def wordBreakCached(s) -> bool:
            if not s:
                return True
            for idx in range(len(s) + 1):
                if s[:idx] in wordSet and wordBreakCached(s[idx:]):
                    return True
            return False
        
        return wordBreakCached(s)

s = Solution()
assert s.wordBreak('leetcode', ['leet', 'code']) == True
assert s.wordBreak(s = "applepenapple", wordDict = ["apple","pen"]) == True
assert s.wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]) == False
long_word = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
aaaa_dict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
assert s.wordBreak(long_word, aaaa_dict) == False