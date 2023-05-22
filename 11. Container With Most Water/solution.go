package main

import "fmt"

func maxArea(height []int) int {
	left := 0
	right := len(height) - 1
	ans := 0
	for left < right {

		if height[left] < height[right] {
			if ans < (right-left)*height[left] {
				ans = (right - left) * height[left]
			}
			left++
		} else {
			if ans < (right-left)*height[right] {
				ans = (right - left) * height[right]
			}
			right--
		}
	}
	return ans

}

func main() {
	height := []int{1, 8, 6, 2, 5, 4, 8, 3, 7}
	fmt.Println(maxArea(height))
}
