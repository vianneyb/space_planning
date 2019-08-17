import copy

SOURCE = {
    "FR_ADM": ["Melanie", "Anne-Dauphine", "Michel", "Magali", "Juliette", "Anne", "Natalia", "Constance", "Faizath",
               "Marion", "Caro"],
    "SE_ADM": ["Anais", "Paola", "Mariel", "Hugo", "Pamela", "Giacomo", "Roddy", "Laura", "Anne_Camille"],
    "NE_ADM": ["Johanna", "Michelle", "Bjarne", "yannique", "Katharina", "Oliver", "Laura", "Nelleke", "Lonneke"],
    "UK_ADM": ["Alexis", "shelbi", "Floriane", "Hattie"],
    "DD_ADM": ["Samy", "Carlos", "Dana"],
    "CC": ["Barbara", "Lisa", "Clara", "Annekatrin", "Katrin", "Veronica", "Vicente", "Veronique", "Annabelle",
           "Celine", "Caroline", "Nabil", "Salome", "Guillaume"],
    "DESTI": ["christophe", "axelle", "dutto", "toto", "tilleul", "jonathan", "theodo1", "theodo2", "theodo3",
              "Arthur"],
    "CRM": ["dudu", "marie", "marie_C", "yushan", "akshita", "mathilde"],
    "OFFER": ["cristina", "jessica", "claire", "Stagiaire_Offer", "Lucie_B", "Lucie_D"],
    "FR_OF": ["Sandrine", "Juliette", "Frederique", "Mathilde", "Severine"],
    "NE_OF": ["Marion", "Philip", "Lisa"],
    "UK_OF": ["Rebecca", "Craig"],
    "SE_OF": ["Silvia", "Marta", "Cristina", "Benedetta"],
    "QUALIF": ["PO_Chloe", "jocelyne", "quentin", "timothe", "Henning"],
    "DATA": ["Adrien", "Renata", "Alexis", "Camille", "Louis", "Aurore", "Stagiaire_Datascience", "Agnes", "Jean",
             "Axel", "Johann", "lead_data_inge", "lead_data_inge", "Data_Mkt"],
    "HP": ["Caro", "Claire", "Alternant_RH", "Julie", "HRBP2", "Marion", "Clement", "HRBP1"],
    "TREX": ["Julien", "benoitSab", "Zigzag", "benoit", "jack", "marc_alex", "chad", "arnaud", "Fiona", "thibaut",
             "erik"],
    "TEA": ["fred", "polval", "skander", "Pablo", "Paul", "lucas", "raph", "tony", "jb", "audrey", "freelance_1",
            "freelance_2", "Pablo"],
    "TIPI": ["julien", "herve", "jean", "sofiane", "loic", "chacha", "sami", "sofiane", "theodo1", "theodo2", "theodo3",
             "adrian"],
    "LAC": ["mariana", "loredana", "sego", "arnaud", "solene", "david", "emmanuel", "flora", "lise", "paula"],
    "NUMBERS": ["Maxime", "Rihab", "Guillaume", "Alexandre", "Arnaud", "AnaisB", "Stagiaire_legal"],
    "INTERNAL": ["renald", "thomas", "emmanuel", "antoineL", "Yoan", "Regis", "RomainQ"],
    "BRAND": ["florian", "fanny", "delphine", "adrien", "clement", "meline", "aurelie", "julien", "resp content",
              "barbara"],
    "INSPI": ["william", "yoann", "thierry", "roxane", "laurent", "elodie", "marine", "Dev_front"],
    "NE_MARKET": ["jenny", "carolin", "verena", "julia", "moniek", "joost", "andrea", "tamara", "dejana", "sanne"],
    "SE_MARKET": ["david", "maria", "soisic", "nuria", "viola", "valeria", "eleonoraD", "eleonoraZ"],
    "UK_MARKET": ["jessica", "anuja", "chloe", "tiphanie"],
    "FR_MARKET": ["emilie", "india", "romain", "chloe", "megan", "chloe", "marionA"],
    "AKI": ["resp_display", "marion", "roland", "clemence", "Medhi", "nicolasC", "Benoit", "juan"],
    "AGENT": ["Agents", "Agents", "Agents", "Agents"],
    "CM - ANNIKA": ["annika"],
    "CM - UK": ["CM UK"],
    "CM - SARAH": ["Sarah"],
    "Arthur": ["arthur"],
    "Vianney": ["vianney"],
    "CODIR - Nas": ["Nas"],
    "CODIR - Daniele": ["Daniele"],
    "CODIR - Laurent": ["Laurent"],
    "CODIR - Benoit": ["Benoit"],
    "CODIR - Amelie": ["Amelie"],

}

TEAMS = {
    "LOCAL_ADM_TIPI_LAC": SOURCE["FR_ADM"] + SOURCE["SE_ADM"] + SOURCE["NE_ADM"] + SOURCE["UK_ADM"] + SOURCE["TEA"] +
                          SOURCE["LAC"],
    "DD_ADM": SOURCE["DD_ADM"],
    "CC": SOURCE["CC"],
    "DESTI_QUALIF_OFFER_LOCAL_OFFER_TIPI": SOURCE["DESTI"] + SOURCE["OFFER"] + SOURCE["QUALIF"] + SOURCE["FR_OF"] +
                                           SOURCE["SE_OF"] + SOURCE["NE_OF"] + SOURCE["UK_OF"] + SOURCE["TIPI"],
    "DATA": SOURCE["DATA"],
    "HP": SOURCE["HP"],
    "TREX": SOURCE["TREX"],
    # "NUMBERS": SOURCE["NUMBERS"],
    # "INTERNAL": SOURCE["INTERNAL"],
    # "AKI-BRAND-CRM-INSPI": SOURCE["AKI"] + SOURCE["BRAND"] + SOURCE["CRM"] + SOURCE["INSPI"],
    # "LOCAL_MARKET": SOURCE["FR_MARKET"] + SOURCE["SE_MARKET"] + SOURCE["NE_MARKET"] + SOURCE["UK_MARKET"],
    # "AGENT": ["Agents", "Agents", "Agents", "Agents"],
    # "CM - ANNIKA": ["annika"],
    # "CM - UK": ["CM UK"],
    # "CM - SARAH": ["Sarah"],
    # "Arthur": ["arthur"],
    # "Vianney": ["vianney"],
    # "CODIR - Nas": ["Nas"],
    # "CODIR - Daniele": ["Daniele"],
    # "CODIR - Laurent": ["Laurent"],
    # "CODIR - Benoit": ["Benoit"],
    # "CODIR - Amelie": ["Amelie"],

}

TEAMS = {
    "A": SOURCE["Arthur"],
    "B": SOURCE["Arthur"],
    "C": SOURCE["CC"],
    "D": SOURCE["Arthur"],
}
# TEAMS = {
#    "DESTI-FULL_OFFER-QUALIF-DATA-TIPI": TEAMS["DESTI"] + TEAMS["OFFER"] + TEAMS["FR-OF"] + TEAMS["NE-OF"] + TEAMS["UK-OF"] + TEAMS["SE-OF"]+ TEAMS["QUALIF"] +TEAMS["DATA"]+TEAMS["TIPI"],
#    "LocalMarketing": TEAMS["FR-MARKET"] + TEAMS["NE-MARKET"] + TEAMS["UK-MARKET"] + TEAMS["SE-MARKET"],
#    "AKI-BRAND+INSPI+CRM": TEAMS["AKI"] + TEAMS["BRAND"] + TEAMS["INSPI"] + TEAMS["CRM"],
#    "ADM-DD-LAC-TEA": TEAMS["TEA"] + TEAMS['FR-ADM'] + TEAMS['SE-ADM'] + TEAMS['NE-ADM'] + TEAMS['UK-ADM'] + TEAMS["laurent"] + TEAMS["LAC"] + TEAMS["DD-ADM"],
#    "NUMBERS+HP": TEAMS["NUMBERS"]+TEAMS["HP"],
#    "CC": 14,
#    "TREX": 12,
#    "INTERNAL": 5,
#
# }


"""
TEAMS = {
    "FR": TEAMS['FR-ADM'] + TEAMS['FR-OF'] + TEAMS['FR-MARKET']+TEAMS['laurent'],
    "UK": TEAMS['UK-ADM'] + TEAMS['UK-OF'] + TEAMS['UK-MARKET'],
    "NE": TEAMS['NE-ADM'] + TEAMS['NE-OF'] + TEAMS['NE-MARKET'],
    "SE": TEAMS['SE-ADM'] + TEAMS['SE-OF'] + TEAMS['SE-MARKET'],
    "CC": 14,
    "TEA-LAC-NUMBERS-HP": TEAMS["TEA"] + TEAMS["LAC"] + TEAMS["NUMBERS"] + TEAMS["HP"],
    "DESTI-TIPI-OFFER-QUALIF-DATA": TEAMS["DESTI"] + TEAMS["TIPI"]+TEAMS["OFFER"]+TEAMS["QUALIF"] + TEAMS["DATA"],
    "INTERNAL": 4,
    "AKI-CRM": TEAMS["AKI"]+TEAMS["CRM"],
    "BRAND+INSPI": TEAMS["BRAND"] + TEAMS["INSPI"],
    "TREX": 12,

}
"""

# arthur vianney nas daniele laurent samy carlos dana
F1 = '1st'
F2 = '2nd'
F3 = '3rd'
F5 = '5th'

FLOORS = {
    F1: 52,
    F2: 58,  # 1 bench
    F3: 72,  # +2 bench + bonus
    F5: 58,  # +2 bench
}


class Team(object):
    def __init__(self, label, members=[]):
        self.members = members
        self.size = len(members)
        self.label = label

    def __str__(self):
        return '%s (%d)' % (self.label, self.size)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.label == other.label

    def __ne__(self, other):
        return self.label != other.label

    def __ge__(self, other):
        return self.label >= other.label

    def __gt__(self, other):
        return self.label > other.label

    def __le__(self, other):
        return self.label <= other.label

    def __lt__(self, other):
        return self.label < other.label

    def __len__(self):
        return self.size


class Floor(object):
    """ Container for items that keeps a running sum """

    def __init__(self, label, size):
        self.size = size
        self.label = label
        self.teams = []
        self.sum = 0

    def append(self, team):
        self.teams.append(team)
        self.sum += team.size

    def fit(self, aTeam):
        if self.size < self.sum + aTeam.size:
            return False
        for team in self.teams:
            if aTeam.label == team.label:
                return False
        return True

    def __str__(self):
        """ Printable representation """
        return 'Floor %s (sum=%d, teams=%s)' % (self.label, self.sum, str(self.teams))

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        self.teams.sort()
        other.teams.sort()
        return self.teams == other.teams

    def __ge__(self, other):
        return self.label >= other.label

    def __gt__(self, other):
        return self.label > other.label

    def __le__(self, other):
        return self.label <= other.label

    def __lt__(self, other):
        return self.label < other.label

    def __contains__(self, item):
        return item in self.teams


class Combinaison(object):
    def __init__(self, floors):
        self.floors = floors

    def check_team_in_floor(self, team, floor):
        for f in self.floors:
            if f.label == floor and team in f:
                return True

        return False

    def is_valid(self):
        if self.check_team_in_floor(Team("TREX"), F1):
            return False
        if not self.check_team_in_floor(Team("AKI-BRAND+INSPI+CRM"), F1):
            return False
        return True

    def __str__(self):
        str = ""
        self.floors.sort()
        for f in self.floors:
            str += "%s\n" % f.__str__()
        return str


def check_teams_same_floor(teamA, teamB, c):
    for floor in c:
        if teamA in floor and teamB in floor:
            return True
    return False


def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


def combine_floor_obj(teams, floor):
    def combine_floor_obj_rec(teams, floor, answers):
        print len(answers)
        for team in teams:
            if floor.fit(team):
                # new branch
                combinaison = copy.deepcopy(floor)
                combinaison.append(team)
                answers.append(combinaison)
                print combinaison
                # try to fill the rest of the branch with the rest of the teams
                reste = copy.copy(teams)
                reste.remove(team)
                combine_floor_obj_rec(reste, combinaison, answers)

    answers = []
    combine_floor_obj_rec(teams, floor, answers)
    return unique(answers)


def count_floor(floor):
    c = 0
    for team in floor:
        c = c + TEAMS[team]
    return c


def compute_teams_not_used(floor, team_list):
    tmp_teams_not_used = copy.copy(team_list)
    for ateam in floor.teams:
        tmp_teams_not_used.remove(ateam)
    return tmp_teams_not_used


combinaisons = []
teams = []
floors = []
for t in TEAMS.iteritems():
    teams.append(Team(t[0], t[1]))

for f in FLOORS.iteritems():
    floors.append(Floor(f[0], f[1]))

print teams
print floors

first = combine_floor_obj(teams, floors[0])
raw_input("fin")
print len(first)
for combi_1st in first:
    teams_not_used = compute_teams_not_used(combi_1st, teams)
    for combi_2nd in combine_floor_obj(teams_not_used, floors[1]):
        teams_not_used2 = compute_teams_not_used(combi_2nd, teams_not_used)

        for combi_3rd in combine_floor_obj(teams_not_used2, floors[2]):
            teams_not_used3 = compute_teams_not_used(combi_3rd, teams_not_used2)

            for combi_5th in combine_floor_obj(teams_not_used3, floors[3]):
                teams_not_used4 = compute_teams_not_used(combi_5th, teams_not_used3)

                if len(teams_not_used4) == 0:
                    combinaison = Combinaison([combi_1st, combi_2nd, combi_3rd, combi_5th])
                    if combinaison.is_valid():
                        combinaisons.append(combinaison)

print len(combinaisons)
satisfied = []
for combinaison in combinaisons:
    print combinaison
    # if not check_team_in_floor('TREX', F1) \
    #        and not check_team_in_floor('DESTI-FULL_OFFER-QUALIF-DATA', F1):
    #    satisfied.append(c)




