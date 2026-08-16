class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = "".join(
            char.lower() for char in s if char.isalnum()
        )

        return stripped == stripped[::-1]
        