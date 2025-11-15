class Solution(object):
    def lengthOfLastWord(self, s):
        splitWord = s.split()
        lastWord = splitWord[-1:]
        return len(lastWord[0])

        