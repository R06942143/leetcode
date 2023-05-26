package main

func rotate(matrix [][]int) {
	n := len(matrix)
	for r := 0; r < n/2; r++ {
		for c := 0; c < (n+1)/2; c++ {
			matrix[r][c], matrix[c][n-1-r], matrix[n-1-r][n-1-c], matrix[n-1-c][r] =
				matrix[n-1-c][r], matrix[r][c], matrix[c][n-1-r], matrix[n-1-r][n-1-c]
		}
	}
}

func main() {
	matrix := [][]int{
		[]int{1, 2, 3},
		[]int{4, 5, 6},
		[]int{7, 8, 9},
	}
	rotate(matrix)
	println(matrix)
}
