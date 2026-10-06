package main

func minAddToMakeValid(s string) int {
	open := 0
	close := 0

	for _, char := range s {
		if char == '(' {
			open++
		} else if open > 0{
			open--
		} else {
			close++
		}
	}
    return open + close
}