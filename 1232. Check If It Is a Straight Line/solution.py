class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        dx = coordinates[1][0] - coordinates[0][0]
        dy = coordinates[1][1] - coordinates[0][1]
        vertical = True
        if dx != 0:
            m = dy / dx
            vertical = False
        for coordinate in range(2, len(coordinates)):
            tmp_x = coordinates[coordinate][0] - coordinates[coordinate - 1][0]
            tmp_y = coordinates[coordinate][1] - coordinates[coordinate - 1][1]
            if not vertical:
                if tmp_x == 0:
                    return False
                tmp_m = tmp_y / tmp_x
                if m != tmp_m:
                    return False
            else:
                if tmp_x != 0:
                    return False
        return True
