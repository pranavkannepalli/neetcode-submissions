class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_end_index = {char:i for i, char in enumerate(s)}
        n = len(s)
        ans = []
        start_index = 0
        end_index = 0
        i = 0
        while i < n:
            end_index = max(last_end_index[s[i]], end_index)
            if i == end_index:
                ans.append(end_index - start_index +1)
            
                start_index = end_index + 1
            i += 1
        return ans
        