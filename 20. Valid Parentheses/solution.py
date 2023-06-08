class Solution:
    def isValid(self, s: str) -> bool:
        validated_stack = []
        converted_map = {")": "(", "}": "{", "]": "["}
        for character in s:
            if character in ["(", "{", "["]:
                validated_stack.append(character)
            else:
                if validated_stack:
                    brackets = validated_stack.pop()
                else:
                    return False
                if converted_map.get(character) != brackets:
                    return False
        if validated_stack == []:
            return True
        else:
            return False
