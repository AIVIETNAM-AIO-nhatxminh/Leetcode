package main

func removeOuterParentheses(s string) string {
	count := 0
	result := []rune{}
    components := []rune{}

	for _, char := range s {
		components = append(components, char)

		if char == '(' {
			count++
		}

		if char == ')' {
			count--
		}

		if count == 0 {
			components = components[1:len(components) - 1]
            result =  append(result, components...)
            components = components[:0]
		}
	}

	return string(result)
}