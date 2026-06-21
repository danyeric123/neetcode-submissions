class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Backtracking approach: build valid parentheses strings character by character
        # Key insight: at any point, we can only add ')' if it doesn't exceed '(' count
        # This ensures we never create invalid strings like ")(" or "())"

        res = []

        def backtrack(curr: str, open_num: int, close_num: int) -> None:
            if open_num == n and close_num == n:
                res.append(curr)
                return
            
            # We can always add another opening
            # since we can add a closing afterwards
            if open_num  < n:
                backtrack(curr+"(", open_num+1, close_num)
            
            # Can only add ')' if it won't exceed number of '('
            # This keeps the string valid at every step
            if close_num < open_num:
                backtrack(curr+")", open_num, close_num+1)

        
        backtrack("",0,0)

        return res