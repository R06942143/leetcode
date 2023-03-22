class Solution:
    def __init__(self):
        self.min_path = float("inf")
        self.road_map = {}
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        for road in roads:
            if not self.road_map.get(road[0]):
                self.road_map[road[0]] = {}
            if not self.road_map.get(road[1]):
                self.road_map[road[1]] = {}
            self.road_map[road[0]][road[1]]=road[2]
            self.road_map[road[1]][road[0]]=road[2]
        self.helper(float("inf"), [], 1, n)
        return self.min_path
        
    def helper(self, score, seen: list, now: int, target: int):
        if now == target:
            self.min_path = min(self.min_path, score)
        for city, path in self.road_map[now].items():
            if city not in seen:
                self.helper(min(score, path), seen + [city], city, target)
        