from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        # Frequency count of each character in the string
        cnt = Counter(s)
        
        vowels = set('aeiou')
        max_vowel = 0
        max_consonant = 0
        
        # Iterate through each character frequency
        for ch, freq in cnt.items():
            if ch in vowels:
                if freq > max_vowel:
                    max_vowel = freq
            else:
                if freq > max_consonant:
                    max_consonant = freq
        
        return max_vowel + max_consonant