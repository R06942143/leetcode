package main

func maximumSubarraySum(nums []int, k int) int64 {
	n := len(nums)
	elements := make(map[int]bool)
	currentSum := int64(0)
	maxSum := int64(0)
	begin := 0

	for end := 0; end < n; end++ {
		if !elements[nums[end]] {
			currentSum += int64(nums[end])
			elements[nums[end]] = true

			if end-begin+1 == k {
				if currentSum > maxSum {
					maxSum = currentSum
				}
				currentSum -= int64(nums[begin])
				delete(elements, nums[begin])
				begin++
			}
		} else {
			for begin < end && nums[begin] != nums[end] {
				currentSum -= int64(nums[begin])
				delete(elements, nums[begin])
				begin++
			}
			begin++
		}
	}
	return maxSum
}

func main() {
	println(maximumSubarraySum([]int{1, 5, 4, 2, 9, 9, 9}, 3))
}
