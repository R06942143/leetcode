package main

import "fmt"

func rotate(nums []int, k int) {
	k = k % len(nums)
	// Fisrt part is nums[:len(nums) -k]
	// Second part is nums[len(nums) - k:]
	tmp := make([]int, len(nums)-k, len(nums)-k)
	for i := 0; i < len(nums)-k; i++ {
		tmp[i] = nums[i]
	}
	copy(nums[:k], nums[len(nums)-k:])
	copy(nums[k:], tmp)
}

func main() {
	nums := []int{1, 2, 3, 4, 5, 6, 7}
	rotate(nums, 3)
	fmt.Println(nums)
}
