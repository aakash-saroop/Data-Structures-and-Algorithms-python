    def isAnagram(self,a,b):
        freq = {}
        # Incrementing frequencies for occurance in the first string
        for character in a:
            if character in freq:
                freq[character] += 1
            else:
               freq[character] = 1 
        # Decrementing frequencies for occurance in the second string 
        for character in b:
            if character in freq:
                freq[character] -= 1
            else:
               freq[character] = -1 
        # check if frequencies of all characters are 0
        for character, count in freq.items():
            if count != 0:
                return False
        return True
