class Solution:
	def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
		m = len(mat)
		rows = sorted(range(m), key=lambda i: (mat[i], i))
		del rows[k:]
		return rows