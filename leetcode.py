#3304. Find the K-th Character in String Game I
'''
Alice and Bob are playing a game. Initially, Alice has a string word = "a".

You are given a positive integer k.

Now Bob will ask Alice to perform the following operation forever:

Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.
For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".

Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.

'''

class Solution(object):
    def kthCharacter(self, k):
        letter = 'a'
        
        while len(letter) < k:
            new_word = ''.join(chr((ord(char) - ord('a') + 1) % 26 + ord('a')) for char in letter)
            letter += new_word
        
        return letter[k - 1] 

