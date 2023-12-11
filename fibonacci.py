def fib(n):
    # Step 2: Base case
    if n==0 or n==1:
        if n==0:
            return 0
        elif n==1:
            return 1
    else: # for other values of n
        # Step 1: Break into subproblems, by calling the same function
        ans = fib(n-1) + fib (n-2)
        return ans
