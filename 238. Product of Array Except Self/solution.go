package main

func productExceptSelf(nums []int) []int {
	ans := []int{}
	for i := 0; i < len(nums); i++ {
		ans = append(ans, 1)
	}
	pre := 1
	last := 1
	for i := 1; i < len(nums); i++ {
		pre *= nums[i-1]
		ans[i] *= pre
	}
	for i := len(nums) - 2; i >= 0; i-- {
		last *= nums[i+1]
		ans[i] *= last
	}
	return ans
}

func main() {
	nums := []int{1, 2, 3, 4}
	productExceptSelf(nums)
}
