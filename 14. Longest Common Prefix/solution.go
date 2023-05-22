package main

func longestCommonPrefix(strs []string) string {
	tmp := strs[0]
	for i := 1; i < len(strs); i++ {
		tmp = compare(tmp, strs[i])
		if tmp == "" {
			return ""
		}
	}
	return tmp
}

func compare(s1, s2 string) string {
	s1n := len(s1)
	s2n := len(s2)
	n := 0
	if s1n > s2n {
		n = s2n
	} else {
		n = s1n
	}
	minN := 0
	for i := 0; i < n; i++ {
		if s1[i] != s2[i] {
			return s1[:minN]
		}
		minN++
	}
	return s1[:minN]
}

func main() {
	strs := []string{"flower", "flow", "flight"}
	longestCommonPrefix(strs)
}
