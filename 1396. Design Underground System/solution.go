package main

type StationTime struct {
	station string
	time    int
}

type ArrialTime struct {
	totalTime int
	times     int
}

type UndergroundSystem struct {
	checkInDict map[int]StationTime
	averageDict map[string]map[string]ArrialTime
}

func Constructor() UndergroundSystem {
	cd := make(map[int]StationTime)
	ad := make(map[string]map[string]ArrialTime)
	us := UndergroundSystem{
		checkInDict: cd,
		averageDict: ad,
	}
	return us
}

func (this *UndergroundSystem) CheckIn(id int, stationName string, t int) {
	this.checkInDict[id] = StationTime{
		station: stationName,
		time:    t,
	}

}

func (this *UndergroundSystem) CheckOut(id int, stationName string, t int) {
	arrialTime := t - this.checkInDict[id].time
	if value, exists := this.averageDict[this.checkInDict[id].station]; exists {
		if at, exists := value[stationName]; exists {
			value[stationName] = ArrialTime{
				times:     at.times + 1,
				totalTime: at.totalTime + arrialTime,
			}
		} else {
			value[stationName] = ArrialTime{
				times:     1,
				totalTime: arrialTime,
			}
		}
	} else {
		this.averageDict[this.checkInDict[id].station] = map[string]ArrialTime{
			stationName: {
				times:     1,
				totalTime: arrialTime,
			},
		}
	}

}

func (this *UndergroundSystem) GetAverageTime(startStation string, endStation string) float64 {
	result := this.averageDict[startStation][endStation]
	return float64(result.totalTime) / float64(result.times)
}

func main() {
	obj := Constructor()
	obj.CheckIn(45, "Leyton", 3)
	obj.CheckIn(32, "Paradise", 8)
	obj.CheckIn(27, "Leyton", 10)
	obj.CheckOut(45, "Waterloo", 15)
	obj.CheckOut(27, "Waterloo", 20)
	obj.CheckOut(32, "Cambridge", 22)
	obj.GetAverageTime("Paradise", "Cambridge")
	obj.GetAverageTime("Leyton", "Waterloo")
	obj.CheckIn(10, "Leyton", 24)
	obj.GetAverageTime("Leyton", "Waterloo")
	obj.CheckOut(10, "Waterloo", 38)
	obj.GetAverageTime("Leyton", "Waterloo")
}
