class Solution:
    def simplifyPath(self, path: str) -> str:
        # need a stack for the double dot
        stack = []
        
        # Split by "/" and filter out empty strings
        parts = [part for part in path.split("/") if part]


        for part in parts:
            if part == "..":
                if stack:
                    # we hit a double dot
                    # but if nothing is in stack
                    # then nothing to go back up to
                    stack.pop()
            elif part != ".":
                stack.append(part)
            
            # we don't do anything if we see a dot
            # since we are remaining in the same folder
        
        return "/" + "/".join(stack)
