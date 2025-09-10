from collections import defaultdict

class Solution:
    def minimumTeachings(self, n, languages, friendships):
        # Convert to sets for faster lookup
        people_languages = [set(langs) for langs in languages]
        
        # Find all people who cannot communicate
        people_to_teach = set()
        for u, v in friendships:
            if people_languages[u-1].isdisjoint(people_languages[v-1]):
                people_to_teach.add(u-1)
                people_to_teach.add(v-1)
        
        # Count how many people can learn each language
        language_count = defaultdict(int)
        for person in people_to_teach:
            for lang in range(1, n+1):  # languages are 1-indexed
                if lang not in people_languages[person]:
                    language_count[lang] += 1
        
        # Minimum number of people to teach
        if language_count:
            return min(language_count.values())
        else:
            return 0
