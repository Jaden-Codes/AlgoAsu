class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        smalls = s.lower()

        while l < r:
            while not smalls[l].isalnum() and l < r:
                l +=1
            while not smalls[r].isalnum() and l < r:
                r-=1
            
            if smalls[l] == smalls[r]:
                l+=1
                r-=1
            else:
                return False
        return True


        