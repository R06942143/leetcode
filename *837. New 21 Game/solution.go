package main

import "fmt"

func new21Game(n int, k int, maxPts int) float64 {
	if k == 0 || n >= k+maxPts {
		return 1
	}
	window := make([]float64, maxPts)
	window[len(window)-1] = 1
	res := float64(0)
	windowSum := float64(1)
	for i := 1; i <= n && windowSum != 0; i++ {
		val := windowSum / float64(maxPts)
		if i >= maxPts && i-maxPts < k {
			windowSum -= window[0]
		}
		window = append(window[1:], val)
		if i >= k {
			res += val
		} else {
			windowSum += val
		}
	}
	return res
}

func main() {
	result := new21Game(21, 17, 10)
	fmt.Println(result)
}
