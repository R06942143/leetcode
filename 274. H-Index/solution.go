package main

import (
	"fmt"
	"sort"
)

func otherPeopleSmartVersionHIndex(citations []int) int {
	m, max := make(map[int]int), 0
	for _, v := range citations {
		// counter map
		m[v]++
	}
	for i, h := 0, len(citations); i <= h; i++ {
		max = i
		h = h - m[i]
	}
	return max
}

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
