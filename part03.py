class Solution:
        def Pow(self, X: int, N: int) -> int:

            # Base Case : If the value of N becomes Zero, then we return 1 as X ^ 0 = 1
            if N == 0:
                return 1

            # Ask Recursion to get previous answer
            partialAns = self.Pow(X, N-1)

            # We multiply it with X to get the answer
            return X * partialAns