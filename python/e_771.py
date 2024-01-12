class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        umap = {}
        sum = 0

        for ch in stones:
            umap[ch] = umap.get(ch, 0) + 1

        for ch in jewels:
            if ch in umap:
                sum = sum + umap[ch]

        return sum
