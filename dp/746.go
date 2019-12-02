package main

import (
	"fmt"
)

func minNumber(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func minCostClimbingStairs(cost []int) int {
	length := len(cost)
	var dp []int
	for i := 0; i < length; i++ {
		if i < 2 {
			dp = append(dp, cost[i])
		} else {
			dp = append(dp, cost[i]+minNumber(dp[i-1], dp[i-2]))
		}
	}
	if length > 1 {
		return minNumber(dp[length-2], dp[length-1])
	}
	return dp[length-1]
}

func main() {
	var b int
	fmt.Print(b)
	arr := [4]int{0, 0, 0, 1}
	// arr := [10]int{1, 100, 1, 1, 1, 100, 1, 1, 100, 1}
	b = minCostClimbingStairs(arr[:])
}

// func haha() int {
// 	fmt.Println(55)
// 	return 2
// }

// minCostClimbingStairs([5]int32{1000.0, 2.0, 3.4, 7.0, 50.0})
