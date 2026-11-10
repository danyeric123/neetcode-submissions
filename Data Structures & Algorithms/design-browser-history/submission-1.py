class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0
        self.size = 1

    def visit(self, url: str) -> None:
        self.curr += 1
        # you are basically throwing away the forward history
        # Because we copy list it ends up being O(n)
        # so instead we use size
        if self.curr == len(self.history):
            self.history.append(url)
            self.size += 1
        else:
            self.history[self.curr] = url
            self.size = self.curr + 1

    def back(self, steps: int) -> str:
        if steps > self.curr:
            self.curr = 0
        else:
            self.curr -= steps
        
        return self.history[self.curr]
        

    def forward(self, steps: int) -> str:
        if steps >= self.size - self.curr:
            # if you are going out of bounds then just go to end
            self.curr = self.size - 1
        else:
            self.curr += steps
        
        return self.history[self.curr]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)