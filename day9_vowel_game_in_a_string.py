class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set("aeiou")
        # If there's at least one vowel, Alice can win.
        for ch in s:
            if ch in vowels:
                return True
        return False
