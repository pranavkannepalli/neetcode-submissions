class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            for i, c in enumerate(s):
                out += str(ord(c)) + ","
            out += "%"
        return out

    def decode(self, s: str) -> List[str]:
        ls = s.split('%')
        out = []
        for string in ls:
            fs = ""
            split = string.split(",")
            for part in split[:-1]:
                fs += chr(int(part))
            out.append(fs)
        return out[:-1]