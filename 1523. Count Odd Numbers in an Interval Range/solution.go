package main

func countOdds(low int, high int) int {
	if low%2 == 1 {
		low = low - 1
	}
	if high%2 == 1 {
		high = high + 1
	}
	return int((high - low) / 2)
}
