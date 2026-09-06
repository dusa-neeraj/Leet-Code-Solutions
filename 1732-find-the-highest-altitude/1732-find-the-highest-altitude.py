class Solution(object):
    def largestAltitude(self, gain):
        current_altitude=0
        highest_altitude=0

        for i in gain:
            current_altitude+=i
            highest_altitude=max(highest_altitude,current_altitude)

        return highest_altitude