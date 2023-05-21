package main

func canCompleteCircuit(gas []int, cost []int) int {
	gasTank := 0
	currTank := 0
	start := 0
	for i := 0; i < len(gas); i++ {
		gasTank += gas[i] - cost[i]
		currTank += gas[i] - cost[i]
		if currTank < 0 {
			start = i + 1
			currTank = 0
		}
	}
	if gasTank < 0 {
		return -1
	} else {
		return start
	}
}

func main() {
	gas := []int{1, 2, 3, 4, 5}
	cost := []int{3, 4, 5, 1, 2}
	canCompleteCircuit(gas, cost)
}
