package main

import "fmt"

func convert(s string, numRows int) string {
	if numRows <= 1 {
		return s
	}
	n := len(s)
	newS := make([]byte, n, n)
	idx := 0
	for i := 0; i < numRows; i++ {
		if i == 0 || i == numRows-1 {
			for j := 0; i+2*j*(numRows-1) < len(s); j++ {
				newS[idx] = s[i+2*j*(numRows-1)]
				idx++
			}
		} else {
			for j := 0; i+2*j*(numRows-1) < len(s); j++ {
				newS[idx] = s[i+2*j*(numRows-1)]
				idx++
				if i+2*j*(numRows-1)+2*(numRows-1-i) < len(s) {
					newS[idx] = s[i+2*j*(numRows-1)+2*(numRows-1-i)]
					idx++
				}
			}
		}
	}
	return string(newS)
}

func main() {
	s := convert("PAYPALISHIRING", 3)
	fmt.Println(s)
}
