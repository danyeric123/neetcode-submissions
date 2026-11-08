class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        res = score = 0
        tokens.sort()

        l, r = 0, len(tokens) - 1

        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                l += 1
                score += 1
                res = max(res, score)
            elif score > 0:
                power += tokens[r]
                r -= 1
                score -= 1
            else:
                # So we do not have an infinite loop
                # if we cannot do anything then just break
                # and also if we get to a point where we
                # cannot use the token then we need to stop or "skip" it
                break

        return res