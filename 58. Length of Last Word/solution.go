package main

import "fmt"

func lengthOfLastWord(s string) int {
	start := false
	result := 0
	for i := len(s) - 1; i >= 0; i-- {
		if !start {
			if s[i] != ' ' {
				start = true
				result++
			}
		} else {
			if s[i] != ' ' {
				result++
			} else {
				return result
			}
		}
	}
	return result
}

func main() {
	s := "Hello World"
	fmt.Println(lengthOfLastWord(s))
}
