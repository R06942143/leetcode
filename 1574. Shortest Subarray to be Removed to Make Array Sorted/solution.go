package main

import "fmt"

func findLengthOfShortestSubarray(arr []int) int {
	right := len(arr) - 1
	left := 0
	for right > 0 && arr[right] >= arr[right-1] {
		right -= 1
	}
	ans := right

	for (left < right) && (left == 0 || arr[left-1] <= arr[left]) {
		for right < len(arr) && arr[left] > arr[right] {
			right += 1
		}
		if ans > right-left-1 {
			ans = right - left - 1
		}
		left += 1
	}

	return ans

}

func main() {
	fmt.Println(findLengthOfShortestSubarray([]int{1, 2, 3, 10, 4, 2, 3, 5}))
}
