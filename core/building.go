package core

import "fmt"

type Building struct {
	Floors []Floor
}

func (building Building) Capacity() int {
	buildingCapacity := 0
	for _, floor := range building.Floors {
		buildingCapacity = buildingCapacity + floor.Size
	}
	return buildingCapacity
}

func (building Building) NbPeopleIn() int {
	nbPeople := 0
	for _, floor := range building.Floors {
		nbPeople = nbPeople + floor.NbPeopleIn
	}
	return nbPeople
}

func (building Building) GetAllDispatchsPossibleWithTeams(teamsList []Team) []Building {
	solutions := []Building{}
	dispatchInFloorsRec(teamsList, building, Building{}, &solutions)
	return solutions
}

func (building Building) IsBigEnoughForTeams(teams []Team) bool {
	nbPeople := 0
	for _, team := range teams {
		nbPeople = nbPeople + team.NbPeople
	}
	fmt.Println("nb people", nbPeople)

	buildingCapacity := building.Capacity()
	fmt.Println("building capacity", buildingCapacity)

	return nbPeople <= buildingCapacity
}

func (b Building) SquadInFloor(squad Squad, floor Floor) bool {
	for _, f := range b.Floors {
		if f.Name == floor.Name {
			for _, team := range floor.Teams {
				for _, s := range team.Squads {
					if s.Name == squad.Name {
						return true
					}
				}
			}
		}

	}
	return false

}

func dispatchInFloorsRec(teamsList []Team, building, aPossibleDispatch Building, solutions *[]Building) {
	combinaisons := building.Floors[0].CalcCombinaisons(teamsList)

	for _, combinaison := range combinaisons {
		teamsLeft := calcTeamsLeft(combinaison.Teams, teamsList)

		if len(teamsLeft) == 0 {
			*solutions = append(*solutions, Building{append(aPossibleDispatch.Floors, combinaison)})
		}
		if len(building.Floors) > 1 {
			dispatchInFloorsRec(teamsLeft, Building{building.Floors[1:]}, Building{append(aPossibleDispatch.Floors, combinaison)}, solutions)
		}
	}
}

func calcTeamsLeft(teamsUsed, teamsList []Team) []Team {
	teamsLeft := []Team{}
	for _, team := range teamsList {
		used := false
		for _, usedTeam := range teamsUsed {
			if usedTeam.Name == team.Name {
				used = true
				break
			}
		}
		if !used {
			teamsLeft = append(teamsLeft, team)
		}
	}
	return teamsLeft
}
