class Solution(object):
    def defangIPaddr(self, address):
        result=""
        for ch in address:
            if ch==".":
                result+="[.]"
            else:
                result += ch

        return result   