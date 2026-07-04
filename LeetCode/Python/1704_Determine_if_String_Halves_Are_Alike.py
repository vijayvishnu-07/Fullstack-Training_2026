# Add your LeetCode solution here
class Solution(object):
    def halvesAreAlike(self, s):
        vowels="a,e,i,o,u,A,E,I,O,U"
        mid=len(s) // 2
        a=s[:mid]
        b=s[mid:]

        count1=0
        count2=0

        for ch in a:
            if ch in vowels:
                count1+=1
        for ch in b:
            if ch in vowels:
                count2+=1

        return count1 == count2
     
        
                
        