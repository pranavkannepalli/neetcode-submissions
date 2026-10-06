class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        minWayToObtain = [[float("infinity")] * 3 for _ in range(3)]

        for i in triplets:
            for j in range(3):
                if i[j] == target[j]:
                    minWayToObtain[j] = [min(minWayToObtain[j][k], i[k]) for k in range(3)]
        
        for minWay in minWayToObtain:
            for j in range(3):
                if minWay[j] > target[j]:
                    return False
        
        return True