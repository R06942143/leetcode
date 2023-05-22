package main

import (
	"fmt"
	"strings"
)

func strStr(haystack string, needle string) int {
	needleN := len(needle)
	haystackN := len(haystack)
	for i := 0; i < haystackN-needleN+1; i++ {
		if haystack[i:i+needleN] == needle {
			return i
		}
	}

	return -1
}

func betterAnswer(haystack string, needle string) int {
	return strings.Index(haystack, needle)
}

func main() {
	fmt.Println(strStr("hello", "ll"))
	fmt.Println(strStr("aaaaa", "bba"))
	fmt.Println(strStr("", ""))
}
