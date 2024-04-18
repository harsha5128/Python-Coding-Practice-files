import heapq
class Solution:
    def minInterval(self, intervals, queries) :
        intervals.sort()
        minHeap = []
        res = {}
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1
                print(l,r)

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries]
    
solution = Solution()
intervals = [[2,3],[2,5],[1,8],[20,25]]
queries = [2,19,5,22]
print(solution.minInterval(intervals, queries)) 

