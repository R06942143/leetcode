package main

import (
	"fmt"
	"sort"
)

func hIndex(citations []int) int {
	sort.Ints(citations)
	hIndex := 0
	for i := len(citations) - 1; i >= 0; i-- {
		if citations[i] > hIndex {
			hIndex++
		} else {
			return hIndex
		}
	}
	return hIndex
}

func main() {
	citations := []int{3, 0, 6, 1, 5}
	fmt.Println(hIndex(citations))
}
