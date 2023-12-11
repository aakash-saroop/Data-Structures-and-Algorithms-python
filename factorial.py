class Solution:
    def factorial (self, N):
        # Step 2: Base case
        if N==0:
            return 1
        else:
            # Step 1: Break into subproblems by calling the same function
            ans = N * self.factorial(N-1)
            return ans
