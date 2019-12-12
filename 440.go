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
	// fmt.Println(math.Min(13, 5))
	// strings.Join([]string{"1, 2, 3, 4, 5, 6, 7, 8, 9", "2"}, "-")
	fmt.Println(findKthNumber(13, 2))
	// fmt.Println(getFirstNumAndLeftover(50, []int{1, 2, 3, 4, 5, 6, 7, 8, 9}, 13, 2))
	// fmt.Println(getFirstNumAndLeftover(13, []int{1, 2, 3, 4, 5, 6, 7, 8, 9}, 3, 2))
	// outer(1, 1)
}

// func outer(a int, b int) {
// 	i := 0
// 	for i < 3 {

// 		_, a, b = inner(a, b, []int{1, 2})
// 		// fmt.Println(i, a, b)
// 		i++
// 	}
// }

// func inner(a int, b int, rg []int) (string, int, int) {
// 	c := a + 1
// 	d := b + 1
// 	return "", c, d
// }

func findKthNumber(n int, k int) int {
	layer, init := 0, 0
	for init <= n {
		init += int(9 * math.Pow(10, float64(layer)))
		layer++
	}
	if layer < 2 {
		return k
	}
	var ret string
	rg := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
	for k > 0 {
		ch := ""
		ch, n, k = getFirstNumAndLeftover(n, k, rg, layer)
		// fmt.Println(n, k)
		ret += ch
		layer--
		rg = []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	}
	res, _ := strconv.Atoi(ret)
	return res
}

// 从左到右的安排每个位置的数：分区间，总数决定每个区间有多少数，通过10的幂运算，此时注意处理区间内可能不饱和的情况
// pool：总数 rg： 区间 target:待分配的数，变化 layer：层级，用来计算当前区间容量和可容纳多少剩余的数
// 返回值：当前最左边的数，下个区间内总数剩余的数，下个区间内目标值剩余的数
func getFirstNumAndLeftover(pool int, target int, rg []int, layer int) (string, int, int) {
	if layer < 2 {
		return strconv.Itoa(rg[target]), 0, 0
	}
	// 这个区间连同坐标有多少个数，不包含多出来不规则的剩余的数
	countCurrentSpan, _ := strconv.Atoi(strings.Repeat("1", layer-1))
	// 多出来不规则的剩余的数-总数，不是待分配
	leftover := pool - len(rg)*countCurrentSpan
	var ret int
	countCanInsert := int(math.Pow(10, float64(layer-1)))
	for _, v := range rg {
		target -= countCurrentSpan
		leftover -= countCurrentSpan
		if target <= countCanInsert {
			return strconv.Itoa(v), leftover, target
		}
		if leftover > 0 {
			if leftover <= countCanInsert {
				target -= leftover
				leftover -= leftover
			} else {
				target -= countCanInsert
				leftover -= countCanInsert
			}
		}
	}
	// strconv.Atoi(s)
	return strconv.Itoa(ret), leftover, target
}
