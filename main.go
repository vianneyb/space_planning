package main

import (
	"fmt"
	"os"
	. "sitting/core"
)

var squadFrADM = Squad{Name: "Fr_Adm", People: []string{"Melanie", "Anne-Dauphine", "Michel", "Magali", "Juliette", "Anne", "Natalia", "Constance", "Faizath", "Marion", "Caro"}}
var squadEsItADM = Squad{Name: "EsIt_Adm", People: []string{"Anais", "Paola", "Mariel", "Hugo", "Pamela", "Giacomo", "Roddy", "Laura", "Anne_Camille"}}
var squadDachNlADM = Squad{Name: "DachNl_Adm", People: []string{"Johanna", "Michelle", "Bjarne", "yannique", "Katharina", "Oliver", "Laura", "Nelleke", "Lonneke"}}
var squadAngloADM = Squad{Name: "Anglo_Adm", People: []string{"Alexis", "shelbi", "Floriane", "Hattie"}}
var squadDestiDevlpmt = Squad{Name: "DestiDevlpmt", People: []string{"Samy", "Carlos", "Dana"}}
var squadCCare = Squad{Name: "CCare", People: []string{"Barbara", "Lisa", "Clara", "Annekatrin", "Katrin", "Veronica", "Vicente", "Veronique", "Annabelle", "Celine", "Caroline", "Nabil", "Salome", "Guillaume"}}
var squadDesti = Squad{Name: "ProductDesti", People: []string{"christophe", "axelle", "dutto", "toto", "tilleul", "jonathan", "theodo1", "theodo2", "theodo3", "Arthur"}}
var squadCRM = Squad{Name: "Crm", People: []string{"dudu", "marie", "marie_C", "yushan", "akshita", "mathilde"}}
var squadXOffer = Squad{Name: "X-Offer", People: []string{"cristina", "jessica", "claire", "Stagiaire_Offer", "Lucie_B", "Lucie_D"}}
var squadFrOffer = Squad{Name: "Fr_Offer", People: []string{"Sandrine", "Juliette", "Frederique", "Mathilde", "Severine"}}
var squadDachNlOffer = Squad{Name: "DachNl_Offer", People: []string{"Marion", "Philip", "Lisa"}}
var squadAngloOffer = Squad{Name: "Anglo_Offer", People: []string{"Rebecca", "Craig"}}
var squadEsItOffer = Squad{Name: "EsIt_Offer", People: []string{"Silvia", "Marta", "Cristina", "Benedetta"}}
var squadQualif = Squad{Name: "ProductQualif", People: []string{"PO_Chloe", "jocelyne", "quentin", "timothe", "Henning"}}
var squadDATA = Squad{Name: "Data", People: []string{"Adrien", "Renata", "Alexis", "Camille", "Louis", "Aurore", "Stagiaire_Datascience", "Agnes", "Jean", "Axel", "Johann", "lead_data_inge", "lead_data_inge", "Data_Mkt"}}
var squadHapPeople = Squad{Name: "HapPeople", People: []string{"Caro", "Claire", "Alternant_RH", "Julie", "HRBP2", "Marion", "Clement", "HRBP1"}}
var squadTREX = Squad{Name: "ProductTrex", People: []string{"Julien", "benoitSab", "Zigzag", "benoit", "jack", "marc_alex", "chad", "arnaud", "Fiona", "thibaut", "erik"}}
var squadTEA = Squad{Name: "ProductTea", People: []string{"fred", "polval", "skander", "Pablo", "Paul", "lucas", "raph", "tony", "jb", "audrey", "freelance_1", "freelance_2", "Pablo"}}
var squadTIPI = Squad{Name: "ProductTipi", People: []string{"julien", "herve", "jean", "sofiane", "loic", "chacha", "sami", "sofiane", "theodo1", "theodo2", "theodo3", "adrian"}}
var squadLocalAgentComnty = Squad{Name: "LocalAgentComnty", People: []string{"mariana", "loredana", "sego", "arnaud", "solene", "david", "emmanuel", "flora", "lise", "paula"}}
var squadNumbers = Squad{Name: "Numbers", People: []string{"Maxime", "Rihab", "Guillaume", "Alexandre", "Arnaud", "AnaisB", "Stagiaire_legal"}}
var squadIntTools = Squad{Name: "InternalTools", People: []string{"renald", "thomas", "emmanuel", "antoineL", "Yoan", "Regis", "RomainQ"}}
var squadBrand = Squad{Name: "Brand", People: []string{"florian", "fanny", "delphine", "adrien", "clement", "meline", "aurelie", "julien", "resp content", "barbara"}}
var squadInspi = Squad{Name: "ProductInspi", People: []string{"william", "yoann", "thierry", "roxane", "laurent", "elodie", "marine", "Dev_front"}}
var squadDachNlMkting = Squad{Name: "DachNl_Mkting", People: []string{"jenny", "carolin", "verena", "julia", "moniek", "joost", "andrea", "tamara", "dejana", "sanne"}}
var squadEsItMkting = Squad{Name: "EsIt_Mkting", People: []string{"david", "maria", "soisic", "nuria", "viola", "valeria", "eleonoraD", "eleonoraZ"}}
var squadAngloMkting = Squad{Name: "Anglo_Mkting", People: []string{"jessica", "anuja", "chloe", "tiphanie"}}
var squadFrMkting = Squad{Name: "Fr_Mkting", People: []string{"emilie", "india", "romain", "chloe", "megan", "chloe", "marionA"}}
var squadAKI = Squad{Name: "Aki", People: []string{"resp_display", "marion", "roland", "clemence", "Medhi", "nicolasC", "Benoit", "juan"}}
var squadAgent = Squad{Name: "AgentDedicated", People: []string{"Agent1", "Agent2", "Agent3", "Agent4"}}

var (
	floor_1st = FloorFactory("1st floor", 52)
	floor_2nd = FloorFactory("2nd floor", 58)
	floor_3rd = FloorFactory("3rd floor", 7)
	floor_5th = FloorFactory("5th floor", 6)
)

// Team{"CM - ANNIKA", []string{"annika"}},
// Team{"CM - UK", []string{"CM UK"}},
// Team{"CM - SARAH", []string{"Sarah"}},
// Team{"Arthur", []string{"arthur"}},
// Team{"Vianney", []string{"vianney"}},
// Team{"CODIR - Nas", []string{"Nas"}},
// Team{"CODIR - Daniele", []string{"Daniele"}},
// Team{"CODIR - Laurent", []string{"Laurent"}},
// Team{"CODIR - Benoit", []string{"Benoit"}},
// Team{"CODIR - Amelie", []string{"Amelie"}},

func main() {

	teams := buildTeams2()
	building := buildBuilding2()

	if !building.IsBigEnoughForTeams(teams) {
		fmt.Println("No enought space in floors to fit everyone !!")
		os.Exit(1)
	}

	solutions := building.GetAllDispatchsPossibleWithTeams(teams)
	fmt.Println(len(solutions))

	// valide des contraintes
	// squadDesti != 1st floor

	// Output solutions
	i := 30
	for _, solution := range solutions {
		if solution.SquadInFloor(squadDesti, floor_1st) {
			continue
		}
		if solution.SquadInFloor(squadTIPI, floor_1st) {
			continue
		}
		if solution.SquadInFloor(squadTEA, floor_1st) {
			continue
		}
		if solution.SquadInFloor(squadTREX, floor_1st) {
			continue
		}

		fmt.Printf("Building: %d / %d:\n", solution.NbPeopleIn(), solution.Capacity())
		i = i - 1
		for _, floor := range solution.Floors {
			fmt.Printf("%s (%d/%d):\t", floor.Name, floor.NbPeopleIn, floor.Size)
			for _, team := range floor.Teams {
				for _, s := range team.Squads {
					fmt.Print(s.Name, " - ")
				}
			}
			fmt.Println("")

		}
		fmt.Println("-------------------------------------------------------")
		if i < 0 {
			break
		}

	}

}

func buildBuilding() Building {
	return Building{Floors: []Floor{
		floor_1st,
		floor_2nd,
		floor_3rd,
		floor_5th,
	}}
}

func buildTeams() []Team {
	return []Team{
		TeamFactory("A6", Squad{"A6", make([]string, 6)}),
		TeamFactory("B14", Squad{"B14", make([]string, 14)}),
		TeamFactory("C10", Squad{"C10", make([]string, 10)}),
		TeamFactory("D2", Squad{"D2", make([]string, 2)}),
		TeamFactory("E10", Squad{"E10", make([]string, 10)}),
		TeamFactory("F10", Squad{"F10", make([]string, 10)}),
		TeamFactory("G10", Squad{"G10", make([]string, 10)}),
		TeamFactory("H3", Squad{"H3", make([]string, 3)}),
		TeamFactory("I6", Squad{"I6", make([]string, 6)}),
		TeamFactory("J7", Squad{"J7", make([]string, 7)}),
	}
}

func buildBuilding2() Building {
	return Building{Floors: []Floor{
		FloorFactory("1st floor", 52),
		FloorFactory("2nd floor", 58),
		FloorFactory("3rd floor", 72),
		FloorFactory("5th floor", 58),
	}}
}

func buildTeams2() []Team {

	return []Team{
		TeamFactory("DD_ADM", squadDestiDevlpmt),
		TeamFactory("CCare", squadCCare),
		TeamFactory("DestiFullOFFER", squadFrOffer, squadDachNlOffer, squadEsItOffer, squadAngloOffer, squadXOffer, squadDesti),
		TeamFactory("QUALIF", squadQualif),
		TeamFactory("DATA", squadDATA),
		TeamFactory("HP", squadHapPeople),
		TeamFactory("TipiTrex", squadTIPI, squadTREX),
		TeamFactory("TeaADMLac", squadDestiDevlpmt, squadFrADM, squadDachNlADM, squadEsItADM, squadAngloADM, squadTEA, squadLocalAgentComnty, squadAgent),
		TeamFactory("NUMBERS", squadNumbers),
		TeamFactory("INTERNAL", squadIntTools),
		TeamFactory("LocalMarketing", squadDachNlMkting, squadEsItMkting, squadAngloMkting, squadFrMkting),
		TeamFactory("InspiAkiLove", squadInspi, squadAKI, squadCRM, squadBrand),
	}
}
