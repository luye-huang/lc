package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

func main() {
	// var a string = "Runoob"
	// var ss string = "abv"
	// ss = ss + ss
	// fmt.Println(strconv.Atoi(strings.Repeat("1", 10)))
	// fmt.Println(getNums(13, 5))
	fmt.Println(getFirstNumAndLeftover(13, []int{1, 2, 3, 4, 5, 6, 7, 8, 9}, 3, 2))
}

func findKthNumber(n int, k int) int {
	layer, init := 0, 0
	for init <= n {
		init += int(9 * math.Pow(10, float64(layer)))
		layer++
	}
	if layer < 2 {
		return k
	}
	// 12 2
	return layer
}

func getFirstNumAndLeftover(pool int, rg []int, target int, layer int) (int, int) {
	countCurrentSpan, _ := strconv.Atoi(strings.Repeat("1", layer-1))
	leftover := pool - len(rg)*countCurrentSpan
	var ret int
	for _, v := range rg {
		target -= countCurrentSpan
		countCanInsert := int(math.Pow(10, float64(layer-1)))
		leftover--
		if leftover > 0 {
			if leftover <= countCanInsert {
				countCanInsert = leftover
				leftover = 0
			} else {
				leftover -= countCanInsert
			}
		}
		if target <= countCanInsert {
			ret = v
			break
		}
	}
	return ret, leftover
}
