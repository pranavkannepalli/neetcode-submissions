class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = [0] * 1001
        m = float("infinity")
        for i in hand:
            counts[i] += 1
            m = min(m, i)
        
        total = len(hand)
        
        while total > 0:
            # subtract every straight you find
            if counts[m] == 0:
                m += 1
            else:
                num = counts[m]
                for i in range(groupSize):
                    if counts[m + i] < num:
                        return False
                    else:
                        counts[m + i] -= num
                        total -= num
        return True