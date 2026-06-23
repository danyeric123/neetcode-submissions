class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        # create a dict of numbers to letter
        num_to_let = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        res = [""]

        for digit in digits:
            res = [prev + new_letter for prev in res for new_letter in num_to_let[digit]]
        
        return res