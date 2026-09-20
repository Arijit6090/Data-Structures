class Solution:
    def integerSquareRoot(self, x):
        if x == 0 or x == 1:
            return x
        sqrt = 1
        while sqrt < x:
            if sqrt * sqrt == x:
                return sqrt
            elif sqrt * sqrt < x:
                sqrt += 1
            else:
                sqrt = sqrt - 1
                return sqrt