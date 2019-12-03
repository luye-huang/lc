package main

import (
	"fmt"
)

// how to create a two dimensional array:
// a := make([][]uint8, dy)
// for i := range a {
//     a[i] = make([]uint8, dx)
// }
// Also note that if you initialize your slice with a composite literal, you get this for "free", for example:

// a := [][]uint8{
//     {0, 1, 2, 3},
//     {4, 5, 6, 7},
// }

func findJudge(N int, trust [][]int) int {
	judges := make([]int, N+1)
	disable := make([]int, N+1)
	dict := make(map[int]map[int]int)
	for _, v := range trust {
		disable[v[0]] = 1
		jud, ok := dict[v[1]]
		if ok {
			if jud[v[1]] != 1 {
				judges[v[1]]++
			}
		} else {
			dictV := make(map[int]int)
			dictV[v[0]] = 1
			dict[v[1]] = dictV
			judges[v[1]]++
		}
	}
	ret := -1
	for k, v := range judges {
		if v == N-1 && disable[k] == 0 && k > 0 {
			ret = k
		}
	}
	return ret
}

func main() {
	var b int
	arr := [][]int{
		{1, 3},
		{1, 4},
		{2, 3},
		{2, 4},
		{4, 3},
	}
	fmt.Print(arr)
	// arr := [10]int{1, 100, 1, 1, 1, 100, 1, 1, 100, 1}
	b = findJudge(4, arr[:][:])
	fmt.Print(b)
}
