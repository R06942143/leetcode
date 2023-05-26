package main

import "fmt"

func setZeroes(matrix [][]int) {
	isJ := false
	isI := false
	for i := 0; i < len(matrix); i++ {
		if matrix[i][0] == 0 {
			isI = true
		}
	}
	for j := 0; j < len(matrix[0]); j++ {
		if matrix[0][j] == 0 {
			isJ = true
		}
	}
	fmt.Println(isI, isJ)
	for i := 1; i < len(matrix); i++ {
		for j := 1; j < len(matrix[0]); j++ {
			if matrix[i][j] == 0 {
				matrix[i][0] = 0
				matrix[0][j] = 0
			}
		}
	}
	for i := 1; i < len(matrix); i++ {
		for j := 1; j < len(matrix[0]); j++ {
			if matrix[i][0] == 0 || matrix[0][j] == 0 {
				matrix[i][j] = 0
			}
		}
	}
	if isI {
		for i := 0; i < len(matrix); i++ {
			matrix[i][0] = 0
		}
	}
	if isJ {
		for j := 0; j < len(matrix[0]); j++ {
			matrix[0][j] = 0
		}
	}
}

func main() {
	matrix := [][]int{
		[]int{1, 2, 3},
		[]int{4, 0, 6},
		[]int{7, 8, 9},
	}
	setZeroes(matrix)
	fmt.Println(matrix)
}
