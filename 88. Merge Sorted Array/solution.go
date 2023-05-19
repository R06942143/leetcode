package main

import "fmt"

func merge(nums1 []int, m int, nums2 []int, n int) {
	mm := m - 1
	nn := n - 1
	now := m + n - 1
	for ; mm >= 0 && nn >= 0; now-- {
		if nums2[nn] >= nums1[mm] {
			nums1[now] = nums2[nn]
			nn--
		} else {
			nums1[now] = nums1[mm]
			mm--
		}
	}
	if nn >= 0 {
		copy(nums1[:nn+1], nums2[:nn+1])
	}
}

func main() {
	nums1 := []int{1, 2, 3, 0, 0, 0}
	nums2 := []int{2, 5, 6}
	merge(nums1, 3, nums2, 3)
	fmt.Println(nums1)
}
