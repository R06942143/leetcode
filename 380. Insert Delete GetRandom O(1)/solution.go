package main

import "math/rand"

type RandomizedSet struct {
	set  map[int]int
	list []int
}

func Constructor() RandomizedSet {
	return RandomizedSet{
		set:  make(map[int]int),
		list: []int{},
	}
}

func (this *RandomizedSet) Insert(val int) bool {
	_, exists := this.set[val]
	if exists {
		return false
	} else {
		this.set[val] = len(this.list)
		this.list = append(this.list, val)
		return true
	}
}

func (this *RandomizedSet) Remove(val int) bool {
	_, exists := this.set[val]
	if exists {
		// Swap this val and update the map
		lastValue := this.list[len(this.list)-1]
		this.list[this.set[val]] = lastValue
		this.set[lastValue] = this.set[val]
		this.list = this.list[:len(this.list)-1]

		delete(this.set, val)
		return true
	} else {
		return false
	}
}

func (this *RandomizedSet) GetRandom() int {
	val := rand.Intn(len(this.set))
	return this.list[val]
}

func main() {
	obj := Constructor()
	param_1 := obj.Insert(1)
	param_2 := obj.Remove(2)
	param_3 := obj.GetRandom()
	println(param_1, param_2, param_3)
}
