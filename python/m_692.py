class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        from collections import defaultdict
        import heapq

        wordCount = defaultdict(int)
        heap = []

        for word in words: wordCount[word] += 1

        for word, count in list(wordCount.items()):
            heapq.heappush(heap, (-count, word))

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res

