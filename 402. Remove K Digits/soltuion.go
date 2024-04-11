func removeKdigits(num string, k int) string {
    stack := []byte{}
    for i := 0; i < len(num); i++ {
        for k > 0 && len(stack) > 0 && stack[len(stack)-1] > num[i] {
            stack = stack[:len(stack)-1] // Pop from stack (efficient slice modification)
            k--
        }
        stack = append(stack, num[i]) // Push current digit only if it's smaller or equal
    }
    for len(stack) != 0 && stack[0] == '0' {
        stack = stack[1:]
    }


    if len(stack) == 0 {
        return "0" // Handle case where all digits are removed
    }
    return string(stack)
    
}

func main() {
	fmt.Println(removeKdigits("1432219", 3)) // 1219
	fmt.Println(removeKdigits("10200", 1)) // 200
	fmt.Println(removeKdigits("10", 2)) // 0
	fmt.Println(removeKdigits("112", 1)) // 11
	fmt.Println(removeKdigits("1234567890", 9)) // 0
}