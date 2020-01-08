class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        letters = string.ascii_lowercase
        shift = sum(shifts)
        result = ''
        for idx, val in enumerate(shifts):
            letter = letters.index(S[idx])
            result += letters[(letter + shift) % 26]
            shift -= val
        return result