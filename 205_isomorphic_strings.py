class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        for schar, tchar in zip(s, t):
            if schar not in mapping:
                mapping[schar] = tchar
            elif mapping[schar] != tchar:
                return False
            else:
                continue
        return len(set(mapping.keys())) == len(set(mapping.values()))

example1 = ('egg', 'add')
example2 = ('foo', 'bar')
example3 = ('paper', 'title')
example4 = ('badc', 'baba')
s = Solution()
assert s.isIsomorphic(*example1) == True
assert s.isIsomorphic(*example2) == False
assert s.isIsomorphic(*example3) == True
assert s.isIsomorphic(*example4) == False
