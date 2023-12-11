    def equilibriumPoint(self,A, N):
        left_sum = 0
        right_sum = 0

        for i in range(1, N):
            right_sum = right_sum + A[i]
            
        if left_sum == right_sum:
            # returning 1 instead of 0
            return 1
            
        else:
            for i in range(1, N):
                right_sum = right_sum - A[i]
                left_sum = left_sum + A[i-1]
                
                if left_sum == right_sum:
                    # returning (i+1) instead of i
                    return (i+1)

            return -1
