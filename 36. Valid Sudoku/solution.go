package main

import "strconv"

func isValidSudoku(board [][]byte) bool {
	rowsMap := [9][9]bool{}
	colsMap := [9][9]bool{}
	gridMap := [9][9]bool{}

	for row := 0; row < 9; row++ {
		for col := 0; col < 9; col++ {
			val, err := strconv.Atoi(string(board[row][col]))
			if err != nil {
				continue
			}
			val--
			gridIndex := col/3 + (row/3)*3
			if rowsMap[row][val] || colsMap[col][val] || gridMap[gridIndex][val] {
				return false
			}
			rowsMap[row][val] = true
			colsMap[col][val] = true
			gridMap[gridIndex][val] = true
		}
	}
	return true
}

func main() {
	board := [][]byte{
		[]byte("53..7...."),
		[]byte("6..195..."),
		[]byte(".98....6."),
		[]byte("8...6...3"),
		[]byte("4..8.3..1"),
		[]byte("7...2...6"),
		[]byte(".6....28."),
		[]byte("...419..5"),
		[]byte("....8..79"),
	}
	result := isValidSudoku(board)
	println(result)
}
