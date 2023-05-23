package main

import "fmt"

func lengthOfLongestSubstring(s string) int {
	stringMap := make(map[byte]int)
	left, right, ans := 0, 0, 0
	for right < len(s) {
		value, exists := stringMap[s[right]]
		if exists {
			if left < value+1 {
				left = value + 1
			}
		}
		stringMap[s[right]] = right
		right++
		if ans < right-left {
			ans = right - left
		}
	}
	return ans
}

func main() {
	s := "abcabcbb"
	fmt.Println(lengthOfLongestSubstring(s))
}
