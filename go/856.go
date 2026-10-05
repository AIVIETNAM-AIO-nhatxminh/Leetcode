package main

import "fmt"

func scoreOfParentheses(s string) int {
	prefix := []int{}
	count := 0
	up := true
	result := 0

	for _, char := range s {
		switch char {
		case '(':
			count++
		case ')':
			count--
		}
		prefix = append(prefix, count)
	}

	fmt.Println(prefix)

	for idx, num := range prefix {
		if idx > 0 {
			if up && num < prefix[idx - 1] {
				result += 1 << (prefix[idx - 1] - 1)
				up = false
			} else if num > prefix[idx - 1] {
				up = true
			}
		} else {
			continue
		}
	}
    return result
}