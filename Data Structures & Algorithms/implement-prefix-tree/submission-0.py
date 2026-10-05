class TreeNode():
    def __init__(self, val=None):
        self.word = False
        self.pointers = [None] * 26

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        curr = self.root
        while len(word) > 0:
            char = word[0]
            if not curr.pointers[ord(char) - 97]:
                curr.pointers[ord(char) - 97] = TreeNode()
            # print(curr.pointers)
            curr = curr.pointers[ord(char) - 97]
            word = word[1:]
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.root
        while len(word) > 0:
            char = word[0]
            if not curr.pointers[ord(char) - 97]:
                return False 
            curr = curr.pointers[ord(char) - 97]
            word = word[1:]
        return curr.word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        while len(prefix) > 0:
            char = prefix[0]
            if not curr.pointers[ord(char) - 97]:
                return False 
            curr = curr.pointers[ord(char) - 97]
            prefix = prefix[1:]
        return True
        