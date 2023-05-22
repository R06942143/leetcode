package main

import "container/heap"

func topKFrequent(nums []int, k int) []int {
	topK := make(map[int]int)
	for _, num := range nums {
		if value, exists := topK[num]; exists {
			topK[num] = value + 1
		} else {
			topK[num] = 1
		}
	}
	t := &topKHeap{}
	heap.Init(t)
	for v, c := range topK {
		heap.Push(t, node{value: v, count: c})
	}
	ans := make([]int, k, k)
	for i := 0; i < k; i++ {
		v := heap.Pop(t).(node)
		ans[i] = v.value
	}
	return ans
}

type node struct {
	count int
	value int
}

type topKHeap []node

func (n topKHeap) Len() int           { return len(n) }
func (n topKHeap) Less(i, j int) bool { return n[i].count > n[j].count }
func (n topKHeap) Swap(i, j int)      { n[i], n[j] = n[j], n[i] }

func (n *topKHeap) Push(x interface{}) {
	*n = append(*n, x.(node))
}

func (n *topKHeap) Pop() interface{} {
	old := *n
	length := len(old)
	result := old[length-1]
	*n = old[0 : length-1]
	return result
}

func main() {
	nums := []int{1, 1, 1, 2, 2, 3}
	k := 2
	topKFrequent(nums, k)
}
