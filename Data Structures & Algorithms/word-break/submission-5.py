class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # cache : word: True | False
        cache = {"": True}
        return self.dp(s, wordDict, cache)

    def dp(self, s, wordDict, cache):        
        if s == "":
            return True

        if s in cache:
            return cache[s]

        for word in wordDict:
            i = s.find(word)
            if i == 0:
                new_word = s[i+len(word):]
                if self.dp(new_word, wordDict, cache):
                    cache[s] = True
                    return cache[s]
                
        cache[s] = False
        return cache[s]
        