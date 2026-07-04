# Add your LeetCode solution here
class Solution(object):
    def firstPalindrome(self, words):
        for word in words:
            if word == word[::-1]:
                return word
        else:
            return ""