package main

import "fmt"

func maxProfit(prices []int) int {
	currProfit := 0
	for i := 1; i < len(prices); i++ {
		if prices[i]-prices[i-1] > 0 {
			currProfit += prices[i] - prices[i-1]
		}
	}
	return currProfit
}

func main() {
	prices := []int{7, 1, 5, 3, 6, 4}
	fmt.Println(maxProfit(prices))
}
