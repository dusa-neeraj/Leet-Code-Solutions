class Solution(object):
    def isPalindrome(self, s):
        new_str=""
        for ch in s:
            if ch.isalnum():
                new_str+=ch.lower()

        left=0
        right=len(new_str)-1
        while left<right:
            if new_str[left]!=new_str[right]:
                return False
            left+=1
            right-=1
            
        return True
        