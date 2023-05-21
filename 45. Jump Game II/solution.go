package main

func jump(nums []int) int {
	if len(nums) == 1 {
		return 0
	}
	preJump := 0
	currJump := nums[0]
	times := 1
	for currJump < len(nums)-1 {
		tmpJump := preJump
		for i := preJump; i <= currJump; i++ {
			if nums[i]+i > tmpJump {
				tmpJump = nums[i] + i
			}
		}
		preJump = currJump
		currJump = tmpJump
		times++
	}
	return times
}

func main() {
	nums := []int{2, 3, 1, 1, 4}
	println(jump(nums))
}
