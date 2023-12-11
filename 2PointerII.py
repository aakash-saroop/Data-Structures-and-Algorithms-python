	def countTriplet(self, arr, n):
	    arr.sort() # O(nlogn)
		count = 0
		for i in range(1, n): # O(n)
		    j = 0
		    k = i-1
		    
		    while j<k: # O(n)
		        if (arr[j]+arr[k] == arr[i]):
		            count = count + 1
		            k = k - 1
		            j = j + 1
		        elif arr[j]+arr[k] < arr[i]:
		            j = j + 1
		        else: 
		            k = k - 1
	    return count
