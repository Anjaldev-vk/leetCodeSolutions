class Solution(object):
    def checkIfPangram(self, sentence):
        str="abcdefghijklmnopqrstuvwxyz"
        for lett in str:
            if lett not in sentence :
                return False
        return True
        