class Solution:
    def isPalindrome(self, s: str) -> bool:
        sreverse = ""
        for ch in s:
            if ch.isalnum():
                sreverse += ch.lower()
        return sreverse == sreverse[::-1]