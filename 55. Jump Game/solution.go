package main

func canJump(nums []int) bool {
	if len(nums) == 1 {
		return true
	}
	lastPosition := nums[0]
	for i := 0; i < lastPosition; i++ {
		if i+nums[i]+1 > lastPosition {
			lastPosition = i + nums[i] + 1
		}
		if i == len(nums)-1 {
			return true
		}
	}
	return false
}

func main() {
	nums := []int{2, 3, 1, 1, 4}
	canJump(nums)
}
