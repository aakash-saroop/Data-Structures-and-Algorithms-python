    def findTriplets(self, arr, n):
        arr.sort() # O(nlogn)
        for i in range(0,n): # O(n)
            j = i+1
            k = n-1
            
            if i==j or j==k or k==i:
                # if any of the values are equal, ignore this combination
                continue
            
            while j!=k: # Two pointer approach O(n) 
                if arr[i] + arr[j] + arr[k] == 0:
                    return 1
                elif arr[i] + arr[j] + arr[k] < 0:
                    j = j + 1
                elif arr[i] + arr[j] + arr[k] > 0:
                    k = k - 1
                    
        return 0
