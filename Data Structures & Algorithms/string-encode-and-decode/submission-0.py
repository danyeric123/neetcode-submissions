class Solution:
    # Special character delimiter is not 
    # enough since all ASCII values are possible
    # we need a way to know how long the word is as
    # well
    def encode(self, strs: List[str]) -> str:
        res = ""
        return "".join([
            str(len(s)) + "#" + s
            for s in strs
        ])

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            # extract the number
            j = i
            while s[j] != "#":
                j += 1
            str_len = int(s[i:j])
            
            # Go from the start
            # after the pound and
            # end the length AFTER
            start = j + 1
            end = start + str_len

            res.append(s[start:end])

            i = end
        
        return res