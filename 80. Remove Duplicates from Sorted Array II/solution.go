package main

import "fmt"

func removeDuplicatesWithTwoPointers(nums []int) int {
	if len(nums) < 2 {
		return len(nums)
	}
	idx := 2
	for i := 2; i < len(nums); i++ {
		if nums[i] != nums[idx-2] {
			nums[idx] = nums[i]
			idx += 1

		}
	}
	return idx
}

func removeDuplicates(nums []int) int {
	seen := make(map[int]int)
	ans := 0
	for i := 0; i < len(nums); i++ {
		value, exists := seen[nums[i]]
		if !exists {
			seen[nums[i]] = 1
			ans++
		} else {
			if value == 2 {
				nums = append(nums[:i], nums[i+1:]...)
				i--
			} else {
				seen[nums[i]] = 2
				ans++
			}
		}
	}
	return ans
}

func main() {
	nums := []int{0, 0, 1, 1, 1, 1, 2, 3, 3}
	removeDuplicates(nums)
	nums1 := []int{0, 0, 1, 1, 1, 1, 2, 3, 3}
	removeDuplicatesWithTwoPointers(nums1)
	fmt.Println(nums)
}
