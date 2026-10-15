class Solution(object):
    def mergeAlternately(self, word1, word2):
        i=0
        j=0
        result=""
        while i<len(word1) or j<len(word2):
            if i<len(word1):
                result = result +  word1[i]
                i+=1
            if j<len(word2):
                result = result+word2[j]
                j+=1
        
        return result
        