class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        height_map = dict()

        for i in range(len(heights)):
            height_map[heights[i]] = names[i]
        
        heights.sort(reverse=True)

        for i in range(len(names)):
            names[i] = height_map[heights[i]]
        
        return names