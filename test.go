package main

import "fmt"

type Floor struct {
	teams []team
}

type team struct {
	name string
}

func combinaisonsRec(floor Floor, teams []team, results *[]Floor) {
	// fmt.Println("--->", floor)
	for k := range teams {
		answer := Floor{append(floor.teams, teams[k])}
		*results = append(*results, answer)
		if len(teams[k+1:]) > 0 {
			combinaisonsRec(answer, teams[k+1:], results)
		}

	}
}

func main() {

	alist := []team{team{"A"}, team{"B"}, team{"C"}, team{"D"}, team{"E"}, team{"F"}, team{"G"}, team{"H"}, team{"I"}, team{"J"}, team{"K"}, team{"L"}, team{"M"}, team{"N"}, team{"O"}, team{"P"}, team{"Q"}, team{"R"}, team{"S"}, team{"T"}, team{"U"}, team{"V"}, team{"W"}} //, team{"X"}, team{"Y"}, team{"Z"}}
	results := []Floor{}

	for k, el := range alist {
		results = append(results, Floor{[]team{el}})
		combinaisonsRec(Floor{[]team{el}}, alist[k+1:], &results)
	}

	fmt.Println(len(results))
	// for _, a := range results {
	// 	fmt.Println(a)
	// }

}
