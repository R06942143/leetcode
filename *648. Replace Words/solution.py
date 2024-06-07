class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        words = sentence.split(" ")
        dictionary.sort(key = lambda x : len(x))

        for i in range(len(words)):
            for root in dictionary:
                if len(words[i]) >= len(root) and words[i][:len(root)] == root:
                    words[i] = root
                    break
            
        return " ".join(words)