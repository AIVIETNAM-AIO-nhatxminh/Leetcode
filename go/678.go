package main

func checkValidString(s string) bool {
	open := []int{}
	star := []int{}
	avail := false
	starIdx := 0

	for idx, char := range s {
		switch char {
		case '(':
			open = append(open, idx)
		case ')':
			if len(open) >= 1 {
				open = open[:len(open) - 1]
			} else if len(star) >= 1 {
				star = star[1: ]
			} else {
				return false
			}
		case '*':
			star = append(star, idx)
		}
	}

	if len(open) > 0 && len(open) > len(star){
		return false
	}


	for _, openPos := range open {
		for i := starIdx; i < len(star); i++ {
			if openPos < star[i] {
				avail = true
				starIdx = i + 1
				break
			}
		}
		if !avail {
			return false
		} else {
			avail = false
		}
	}

    return true
}