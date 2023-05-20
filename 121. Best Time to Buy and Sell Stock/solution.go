package main

import "fmt"

func maxProfit(prices []int) int {
	buy := prices[0]
	currProfit := 0
	for i := 1; i < len(prices); i++ {
		if prices[i]-buy > currProfit {
			currProfit = prices[i] - buy
		}
		if prices[i] < buy {
			buy = prices[i]
		}
	}
	return currProfit
}

func main() {
	prices := []int{7, 1, 5, 3, 6, 4}
	fmt.Println(maxProfit(prices))

}
