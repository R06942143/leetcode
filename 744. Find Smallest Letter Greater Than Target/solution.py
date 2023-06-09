class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        find = ""
        for character in letters:
            if character > target:
                if find == "" or character < find:
                    return character
        return letters[0]
