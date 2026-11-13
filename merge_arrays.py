class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        min_len = min(len1, len2)
        max_len = max(len1, len2)
        diff = max_len - min_len
        merged_word = ""


        for i, j in zip(word1, word2):
            merged_word = merged_word + i
            merged_word = merged_word + j

        if len1 > len2 :
            for i in range(len2, len1):
                merged_word = merged_word + word1[i]
        else:
            for i in range(len1, len2):
                merged_word = merged_word + word2[i]
        return merged_word


solution = Solution()
word1 = "ab"
word2 = "pqrst"
result = solution.mergeAlternately(word1, word2)
print(result)
