package core

// Floor
type Floor struct {
	Teams      []Team
	Size       int
	Name       string
	NbPeopleIn int
}

// Fit check if a given Team will fit in the floor
func (floor Floor) Fit(team Team) bool {
	return floor.NbPeopleIn+team.NbPeople <= floor.Size
}

// FloorFactory return a new Floor
func FloorFactory(name string, size int) Floor {
	return Floor{[]Team{}, size, name, 0}
}

func floorFactoryFull(name string, size int, teams []Team) Floor {
	nbPeople := 0
	for _, team := range teams {
		nbPeople += team.NbPeople
	}
	return Floor{teams, size, name, nbPeople}
}

// WithTeam return a new Floor with the team added in it
func (floor Floor) WithTeam(team Team) Floor {

	// ----
	teams := make([]Team, len(floor.Teams)+2)
	k := 0
	for _, t := range floor.Teams {
		teams[k] = t
		k++
	}
	teams[k+1] = team
	// ---> could have use append but some weird memory overlap happened
	return floorFactoryFull(floor.Name, floor.Size, teams)
}

// CalcCombinaisons compute all the unique combinaison of Teams in a given Floor
func (floor Floor) CalcCombinaisons(teamsList []Team) []Floor {
	results := []Floor{}

	for k, team := range teamsList {
		if floor.Fit(team) {
			result := floor.WithTeam(team)
			results = append(results, result)
			calcCombinaisonsFloorRec(result, teamsList[k+1:], &results)
		}
	}
	return results
}

func calcCombinaisonsFloorRec(floor Floor, teams []Team, results *[]Floor) {
	for k, team := range teams {
		if floor.Fit(team) {

			result := floor.WithTeam(team)

			*results = append(*results, result)
			if len(teams) > k+1 {
				calcCombinaisonsFloorRec(result, teams[k+1:], results)
			}
		}

	}
}
