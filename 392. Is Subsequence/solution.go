package main

func isSubsequence(s string, t string) bool {
	if len(s) == 0 {
		return true
	}
	if len(s) > len(t) {
		return false
	}
	sIdx := 0
	for i := 0; i < len(t); i++ {
		if t[i] == s[sIdx] {
			sIdx++
		}
		if sIdx == len(s) {
			return true
		}
	}
	return sIdx == len(s)
}

func main() {
	isSubsequence("abc", "ahbgdc")
}
