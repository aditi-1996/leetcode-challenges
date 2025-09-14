class Solution:
    def spellchecker(self, wordlist, queries):
        vowels = set('aeiou')

        def devowel(s: str) -> str:
            # Replace vowels with '*'
            return ''.join('*' if c in vowels else c for c in s)

        # 1) Exact matches
        exact = set(wordlist)

        # 2) Case-insensitive first-occurrence map
        lower_map = {}
        # 3) Vowel-error map on lowercased + devoweled form
        vowel_map = {}

        for w in wordlist:
            lw = w.lower()
            lower_map.setdefault(lw, w)
            vowel_map.setdefault(devowel(lw), w)

        ans = []
        for q in queries:
            if q in exact:
                ans.append(q)
                continue
            lq = q.lower()
            if lq in lower_map:
                ans.append(lower_map[lq])
                continue
            vq = devowel(lq)
            ans.append(vowel_map.get(vq, ""))

            # If none matched, append "" (as required)
        return ans