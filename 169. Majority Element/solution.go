package main

import "fmt"

func majorityElement(nums []int) int {
	seen := make(map[int]int)
	for _, num := range nums {
		value, exists := seen[num]
		if !exists {
			seen[num] = 1
		} else {
			seen[num] = value + 1
		}
		if value >= len(nums)/2 {
			return num
		}
	}
	return -1
}

func main() {
	nums := []int{3, 2, 3}
	result := majorityElement(nums)
	fmt.Println(result)
}
