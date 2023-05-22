package main

import (
	"bytes"
	"fmt"
	"strings"
)

func fullJustify(words []string, maxWidth int) []string {
	justify := []string{}
	current, curLength := []string{}, 0
	for i, w := range words {
		if curLength+len(current)+len(w) > maxWidth {
			if len(current) == 1 {
				// only one word, all spaces are to the right of the word
				curLine := current[0] + strings.Repeat(" ", maxWidth-len(current[0]))
				justify = append(justify, curLine)
			} else {
				diff := maxWidth - curLength
				spaces := diff / (len(current) - 1)
				more := diff % (len(current) - 1)
				curLine := bytes.Buffer{}
				for ci, cw := range current {
					curLine.WriteString(cw)
					if ci != len(current)-1 {
						moreBlanks := 0
						if more > 0 {
							moreBlanks = 1
							more--
						}
						curLine.WriteString(strings.Repeat(" ", spaces+moreBlanks))
					}
				}
				justify = append(justify, curLine.String())
			}
			current, curLength = []string{}, 0
		}

		curLength += len(w)
		current = append(current, w)

		// last line, left justified and no extra space is inserted between words
		if i == len(words)-1 {
			lastLine := strings.Join(current, " ")
			lastLine = lastLine + strings.Repeat(" ", maxWidth-len(lastLine))
			justify = append(justify, lastLine)
		}
	}
	return justify
}

func main() {
	words := []string{"This", "is", "an", "example", "of", "text", "justification."}
	maxWidth := 16
	justify := fullJustify(words, maxWidth)
	fmt.Println(justify)
}
