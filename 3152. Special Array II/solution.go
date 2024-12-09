package main

import "fmt"

func isArraySpecial(nums []int, queries [][]int) []bool {
	prefixSum := make([]int, len(nums))

	for i := 1; i < len(nums); i++ {
		prefixSum[i] = prefixSum[i-1]
		if nums[i]%2 != nums[i-1]%2 {
			prefixSum[i]++
		}
	}
	ans := make([]bool, len(queries))
	for i := 0; i < len(queries); i++ {
		if prefixSum[queries[i][1]]-prefixSum[queries[i][0]] == queries[i][1]-queries[i][0] {
			ans[i] = true
		}
	}
	return ans
}

func main() {
	nums := []int{1, 2, 3, 4, 5}
	queries := [][]int{{0, 2}, {1, 3}, {2, 4}}
	fmt.Println(isArraySpecial(nums, queries))
}
