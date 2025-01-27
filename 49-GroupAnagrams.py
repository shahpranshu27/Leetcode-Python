class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = collections.defaultdict(list)

        # here, string on all indices will get sorted, then it will make different sorted string as key. eg: for key 'aet', it will check "eat", then for key 'ant, it will check "tan" etc..
        for word in strs:
            sorted_word=''.join(sorted(word))
            dict1[sorted_word].append(word)
        
        return list(dict1.values())
