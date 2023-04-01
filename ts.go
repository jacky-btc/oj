package main

import (
	"fmt"
)

func main() {
	a := 1.5
	var b float32 = 1
	c := float32(a)-b
	if c == 0.2 {
		fmt.Print("eq")
	}else {
		fmt.Print(c)
	}
}

