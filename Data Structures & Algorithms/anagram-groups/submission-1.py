class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            anagrams[key].append(s)
        
        return [anagram_list for _, anagram_list in anagrams.items()]