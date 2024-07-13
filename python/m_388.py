class Solution:
    def lengthLongestPath(self, input):
        # pathlen dict keeps track of the dir lengths up until that point
        # then we just check if there is a file and update the max
        # python treats \t as one char in len (understandably so)
        if "." not in input: return 0
        maxlen = 0
        pathlen = {0: 0}
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1
        return maxlen
