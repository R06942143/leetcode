class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        out_img = [[0] * len(img[0]) for _ in range(len(img))]
        for i in range(len(img)):
            for j in range(len(img[0])):
                total = 0
                count = 0
                for x in (i - 1, i, i + 1):
                    for y in (j - 1, j, j + 1):
                        if 0 <= x < len(img) and 0 <= y < len(img[0]):
                            total += img[x][y]
                            count += 1
                out_img[i][j] = total // count
        return out_img