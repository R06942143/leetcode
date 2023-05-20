package main

import "fmt"

func removeDuplicates(nums []int) int {
	seen := map[int]bool{}
	for i := 0; i < len(nums); i++ {
		_, exist := seen[nums[i]]
		if exist {
			nums = append(nums[:i], nums[i+1:]...)
			fmt.Println("exist", nums[i], nums)
			i--
		} else {
			seen[nums[i]] = true
		}
	}
	return len(seen)
}

func main() {
	// nums := []int{1, 1, 2}
	nums := []int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4}
	k := removeDuplicates(nums)
	fmt.Println(k, nums)
}
