    def isPalindrome(self, S):
        for i in range(0, len(S)//2):
            if S[i] != S[len(S)-i-1]:
                return 0
        return 1
