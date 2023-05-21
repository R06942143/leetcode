package main

import "fmt"

func trap(height []int) int {
	leftMax := height[0]
	rightMax := height[len(height)-1]
	leftIdx := 1
	rightIdx := len(height) - 2
	ans := 0
	for leftIdx <= rightIdx {
		if leftMax < rightMax {
			if height[leftIdx] >= leftMax {
				leftMax = height[leftIdx]
			} else {
				ans += leftMax - height[leftIdx]
			}
			leftIdx++
		} else {
			if height[rightIdx] >= rightMax {
				rightMax = height[rightIdx]
			} else {
				ans += rightMax - height[rightIdx]
			}
			rightIdx--
		}
	}
	return ans
}

func main() {
	height := []int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}
	fmt.Println(trap(height))
}
