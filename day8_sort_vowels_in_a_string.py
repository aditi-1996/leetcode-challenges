class Solution:
    def sortVowels(self, s: str) -> str:
        VOWELS = set("aeiouAEIOU")
        # 1) Extract vowels and sort them
        vowels = sorted([c for c in s if c in VOWELS])
        # 2) Reconstruct string replacing vowels with sorted ones
        res = []
        vi = 0
        for c in s:
            if c in VOWELS:
                res.append(vowels[vi])
                vi += 1
            else:
                res.append(c)
        return "".join(res)

# Example
if __name__ == "__main__":
    print(Solution().sortVowels("lEetcOde"))  # -> "lEOtcede"
