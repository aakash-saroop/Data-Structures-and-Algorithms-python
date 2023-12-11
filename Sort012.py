class Solution:
    def sort012(self,arr,n):

        # Counting the number of elements of each value
        count_zero = 0
        count_one = 0
        count_two = 0
        for i in range(0, n):
            if arr[i] == 0:
                count_zero = count_zero + 1
            elif arr[i] == 1:
                count_one = count_one + 1
            else:
                count_two = count_two + 1
                
        # zero_ending_index: Index before which all 0s should be arranged
        # one_ending_index: Index before which all 1s should be arranged
        #two_ending_index: Index before which all 2s should be arranged
        zero_ending_index = count_zero
        one_ending_index = count_zero + count_one
        two_ending_index = count_zero + count_one + count_two

        # Arranging all 0s, then 1s, then 2s 
        for i in range(0, zero_ending_index):
            arr[i] = 0
        for i in range(zero_ending_index, one_ending_index):
            arr[i] = 1
        for i in range(one_ending_index, two_ending_index):
            arr[i] = 2
            
        return arr
