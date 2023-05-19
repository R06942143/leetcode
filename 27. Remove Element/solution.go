package main

func removeElement(nums []int, val int) int {
	count := 0
	for i := 0; i < len(nums); i++ {
		if val == nums[i] {
			nums = append(nums[:i], nums[i+1:]...)
			i--
		} else {
			count++
		}
	}
	return count
}

func main() {
	nums := []int{3, 2, 2, 3}
	val := 3
	println(removeElement(nums, val))
}
