package main

func average(salary []int) float64 {
	var all int
	maxSalary := salary[0]
	minSalary := salary[0]
	for _, money := range salary {
		if money > maxSalary {
			maxSalary = money
		}
		if money < minSalary {
			minSalary = money
		}
		all += money
	}
	return float64(all-maxSalary-minSalary) / float64(len(salary)-2)
}
