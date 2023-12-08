package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func is_winning_num(num string, list []string) bool {
	for _, winning_num := range list {
		if num == winning_num {
			return true
		}
	}
	return false
}

func main() {
	filePath := "day.data"
	content, err := ioutil.ReadFile(filePath)
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	// total_points := 0.0
	lines := strings.Split(string(content), "\n")
	var winner_counts []int
	initial_card_counts := make([]int, len(lines))
	for _ , value := range lines {
		split_line := strings.Split(value, "|")
		card := split_line[0]
		my_nums := strings.Fields(strings.TrimSpace(split_line[1]))
		card_nums := strings.Fields(strings.TrimSpace(strings.Split(card, ":")[1]))

		winner_count := 0
		for _, my_num := range my_nums {
			if is_winning_num(my_num, card_nums) {
				winner_count += 1
			}
		}
		winner_counts = append(winner_counts, winner_count)
		for i := range initial_card_counts {
			initial_card_counts[i] = 1
		}
		// var card_points float64 = math.Pow(2, float64(winner_count - 1))
		// fmt.Printf("Found %d winners. Total points for the card: %f\n", winner_count, card_points)
		// if winner_count > 0 {
		// 	total_points += math.Pow(2, float64(winner_count - 1))
		// }
	}
	

	for i, winner_count := range winner_counts {
		for j := 1; j <= winner_count; j++ {
			initial_card_counts[i + j] += initial_card_counts[i]
		}
	}
	slice_sum := 0
	for _, item := range initial_card_counts {
		slice_sum += item
	}
	fmt.Printf("%d\n", slice_sum)
	// fmt.Printf("Total Points: %f", total_points)
}