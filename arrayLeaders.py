    def leaders(self, A, N):
        A_util = [0]*N
        maximum = A[N-1]
        A_util[N-1] = A[N-1]
        
        for i in range(N-2, -1, -1): # O(N)
            A_util[i] = maximum
            if A[i] > maximum:
                maximum = A[i]
                
        ans = []
        for i in range(0,N): # O(N)
            if A[i] >= A_util[i]:
                ans.append(A[i])
                
        return ans
