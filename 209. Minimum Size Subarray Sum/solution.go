package main

import "fmt"

func twoPointers(target int, nums []int) int {
	i, res := 0, len(nums)+1
	for j := 0; j < len(nums); j++ {
		target -= nums[j]
		for target <= 0 {
			if res > j-i+1 {
				res = j - i + 1
			}
			target += nums[i]
			i++
		}
	}
	return res % (len(nums) + 1)
}

func main() {
	target := 7
	nums := []int{2, 3, 1, 2, 4, 3}
	fmt.Println(twoPointers(target, nums))
}
