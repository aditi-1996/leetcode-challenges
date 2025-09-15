class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)  # put broken letters in a set for O(1) lookup
        count = 0
        
        for word in text.split():
            # if none of the letters in word are broken, count it
            if not any(ch in broken for ch in word):
                count += 1