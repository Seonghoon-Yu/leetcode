def groupAnagrams(self, strs):
    anagrams = collections.defaultdict(list)

    for word in strs:
        # list 벗기기 위해 .join 이용
        anagrams[''.join(sorted(word))].append(word)

    return anagrams.values()
