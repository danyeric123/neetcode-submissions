class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        self.curr += 1
        # you are basically throwing away the forward history
        # Because we copy list it ends up being O(n)
        self.history = self.history[:self.curr] + [url]

    def back(self, steps: int) -> str:
        if steps > self.curr:
            self.curr = 0
        else:
            self.curr -= steps
        
        return self.history[self.curr]
        

    def forward(self, steps: int) -> str:
        if steps >= len(self.history) - self.curr:
            # if you are going out of bounds then just go to end
            self.curr = len(self.history) - 1
        else:
            self.curr += steps
        
        return self.history[self.curr]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)