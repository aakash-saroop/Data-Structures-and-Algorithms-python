def numberOfPaths(m, n):
        # Step 2: Base case
        if m==1 or n==1:
            return 1
        # Step 1: Break into sub problems by calling the same function
        return (numberOfPaths(m, n-1) + numberOfPaths(m-1, n))
