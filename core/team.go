package core

type Squad struct {
	Name   string
	People []string
}

// Team represents a group of squads
type Team struct {
	Name     string
	NbPeople int
	Squads   []Squad
}

// TeamFactory build a team from many squads
func TeamFactory(name string, squads ...Squad) Team {
	team := Team{name, 0, []Squad{}}
	for _, squad := range squads {
		team.NbPeople += len(squad.People)
		team.Squads = append(team.Squads, squad)
	}
	return team
}
