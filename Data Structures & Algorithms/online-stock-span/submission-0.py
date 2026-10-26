class StockSpanner:
    # You will want a monotonically non-increasing
    # stack since if we have the next stock price
    # not be more or equal to the previous then its
    # span will be 1 since its neighbor is larger

    def __init__(self):
        # stack of price and span
        # since it saves calculations
        self._stack = []

    def next(self, price: int) -> int:
        # span is at least today
        span = 1

        while self._stack and self._stack[-1][0] <= price:
            # Add span of lower price
            span += self._stack.pop()[1]
        
        # add this to the stack
        # We do not need the previous ones
        # since we are keeping track of the span
        # of prices
        self._stack.append((price, span))
        print(self._stack)

        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)