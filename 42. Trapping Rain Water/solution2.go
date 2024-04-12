package main

import "fmt"


func trap(height []int) int {
    var waterStored int
    leftElevationPoint, rightElevationPoint := 0, len(height) - 1
    maxLeftElevation, maxRightElevation := height[leftElevationPoint], height[rightElevationPoint]

    for leftElevationPoint < rightElevationPoint{
        if maxLeftElevation < maxRightElevation {
            leftElevationPoint++
            if height[leftElevationPoint] > maxLeftElevation{
                maxLeftElevation = height[leftElevationPoint]
            }
            waterStored += maxLeftElevation - height[leftElevationPoint]
        } else {
            rightElevationPoint--
            if height[rightElevationPoint] > maxRightElevation {
                maxRightElevation = height[rightElevationPoint]
            }
            waterStored += maxRightElevation - height[rightElevationPoint]
        }
    }

    return waterStored
}

func main() {
	height := []int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}
	fmt.Println(trap(height))
}