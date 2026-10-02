class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        c = [[position[i], self.stepsToGet(target, position[i], speed[i])] for i in range(len(position))]
        c.sort(key=lambda item: item[0])
        
        fleets = 1
        lead = c.pop()
        while len(c) != 0:
            curr = c.pop()
            if curr[1] > lead[1]:
                fleets += 1
                lead = curr
        return fleets 

    def stepsToGet(self, target: int, pos: int, sp: int):
        return (target - pos)/sp