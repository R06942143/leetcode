package main

func twoSum(numbers []int, target int) []int {
	left := 0
	right := len(numbers) - 1
	for left < right {
		switch num := numbers[left] + numbers[right]; {
		case num > target:
			right--
		case num < target:
			left++
		default:
			return []int{left + 1, right + 1}
		}
	}
	return []int{left + 1, right + 1}
}

func main() {
	twoSum([]int{2, 7, 11, 15}, 9)
}
