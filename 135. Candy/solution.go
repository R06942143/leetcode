package main

import "fmt"

func candy(ratings []int) int {
	ans := make([]int, len(ratings))
	ans[0] = 1
	for i := 1; i < len(ratings); i++ {
		if ratings[i] > ratings[i-1] {
			ans[i] = ans[i-1] + 1
		} else {
			ans[i] = 1
		}
	}
	result := ans[len(ratings)-1]
	for i := len(ratings) - 2; i >= 0; i-- {
		if ratings[i] > ratings[i+1] {
			if ans[i] < ans[i+1]+1 {
				ans[i] = ans[i+1] + 1
			}
		}
		result += ans[i]
	}
	return result
}

func main() {
	ratings := []int{1, 2, 2}
	fmt.Println(candy(ratings))
}
