package main

import (
	"fmt"
	"strings"
)

func reverseWords(s string) string {
	wordSlice := strings.Fields(s)
	reversedSlice := reverse(wordSlice)
	return strings.Join(reversedSlice, " ")
}

func reverse(s []string) []string {
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		s[i], s[j] = s[j], s[i]
	}
	return s
}

func main() {
	s := reverseWords("the sky is blue")
	fmt.Println(s)
}
