package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func main() {
	filePath := "day.data"
	content, err := ioutil.ReadFile(filePath)
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	lines := strings.Split(string(content), "\n")
	for _ , value := range lines {
		split_line := strings.Split(value, "|")
		card := split_line[0]
		my_nums := split_line[1]
		card_nums := strings.Split(strings.TrimSpace(strings.Split(card, ":")[1]), " ")
		fmt.Printf("Card: %d, my_nums %d\n", card_nums, my_nums)
	}
}