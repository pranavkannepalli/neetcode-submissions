class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        c = [[position[i], speed[i], self.stepsToGet(target, position[i], speed[i])] for i in range(len(position))]
        c.sort(key=lambda item: -item[0])
        
        fleets = 1
        # print(c)
        lead = c.pop(0)
        while len(c) != 0:
            # print(c)
            curr = c.pop(0)
            if curr[2] > lead[2]:
                # print("adding")
                fleets += 1
                lead = curr
        return fleets 

    def stepsToGet(self, target: int, pos: int, sp: int):
        return (target - pos)/sp
        # return math.ceil((target - pos)/sp)