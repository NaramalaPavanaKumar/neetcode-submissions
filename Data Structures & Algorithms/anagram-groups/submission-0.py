class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp=defaultdict(list)
        for word in strs:
            c=[0]*26
            for ch in word:
                i=ord(ch)-ord('a')
                c[i]+=1

            key=tuple(c)
            grp[key].append(word)
        return list(grp.values())

            
        