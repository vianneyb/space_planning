TEAMS = {
    "laurent": 1,
    "FR-ADM": 11,
    "SE-ADM": 10,
    "NE-ADM": 8,
    "UK-ADM": 4,
    "DD-ADM": 2,
    "CC": 14,
    "DESTI": 9,
    "CRM": 6,
    "OFFER": 7,
    "FR-OF": 5,
    "NE-OF": 2,
    "UK-OF": 2,
    "SE-OF": 4,
    "QUALIF": 4,
    "DATA": 14,
    "HP": 8,
    "TREX": 12,
    "TEA": 12,
    "TIPI": 10,
    "LAC": 10,
    "NUMBERS": 8,
    "INTERNAL": 4,
    "BRAND": 10,
    "INSPI": 8,
    "NE-MARKET": 11,
    "SE-MARKET": 8,
    "UK-MARKET": 4,
    "FR-MARKET": 8,
    "AKI": 12,
}

TEAMS = {
    "DESTI-FULL_OFFER-QUALIF-DATA-TIPI": TEAMS["DESTI"] + TEAMS["OFFER"] + TEAMS["FR-OF"] + TEAMS["NE-OF"] + TEAMS["UK-OF"] + TEAMS["SE-OF"]+ TEAMS["QUALIF"] +TEAMS["DATA"]+TEAMS["TIPI"],
    "LocalMarketing": TEAMS["FR-MARKET"] + TEAMS["NE-MARKET"] + TEAMS["UK-MARKET"] + TEAMS["SE-MARKET"],
    "AKI-BRAND+INSPI+CRM": TEAMS["AKI"] + TEAMS["BRAND"] + TEAMS["INSPI"] + TEAMS["CRM"],
    "ADM-DD-LAC-TEA": TEAMS["TEA"] + TEAMS['FR-ADM'] + TEAMS['SE-ADM'] + TEAMS['NE-ADM'] + TEAMS['UK-ADM'] + TEAMS["laurent"] + TEAMS["LAC"] + TEAMS["DD-ADM"],
    "NUMBERS+HP": TEAMS["NUMBERS"]+TEAMS["HP"],
    "CC": 14,
    "TREX": 12,
    "INTERNAL": 5,

}



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


FLOORS = {
    "1st": 52,
    "2nd": 58,  # 1 bench
    "3rd": 72,  # +2 bench + bonus
    "5th": 58,  # +2 bench
}




import copy


class Team(object):
    def __init__(self, label, size):
        self.size = size
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
        self.teams.sort()
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


def check_teams_same_floor(teamA, teamB, c):
    for floor in c:
        if teamA in floor and teamB in floor:
            return True
    return False


def check_team_in_floor(teamA, floor):
    return teamA in floor


def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


def combine_floor(teams, nb_places):
    answers = []

    for team in teams:
        if TEAMS[team] > nb_places:
            continue
        answer_size = TEAMS[team]
        answer = [team]
        for team in teams:
            size = TEAMS[team]
            if answer_size + size <= nb_places and team not in answer:
                answer.append(team)
                answer_size += size
        answer.sort()
        answers.append(answer)
    answers.sort()
    return unique(answers)


def combine_floor_obj(teams, floor):
    answers = []

    for team in teams:
        if not floor.fit(team):
            continue

        combinaison = copy.deepcopy(floor)
        combinaison.append(team)

        for team in teams:
            if not combinaison.fit(team):
                continue

            combinaison_rec = copy.deepcopy(combinaison)
            combinaison_rec.append(team)
            for team2 in teams:
                if not combinaison_rec.fit(team2):
                    continue
                combinaison_rec.append(team2)
            answers.append(combinaison_rec)
        answers.append(combinaison)
    answers.sort()
    print answers
    return unique(answers)


def combine_floor_obj(teams, floor):
    """
        [FR-ADM (4), laurent (5), SE-ADM (3), NE-ADM (6)] Floor 5th (sum=0, teams=[])
            [laurent (5), SE-ADM (3), NE-ADM (6)] Floor 5th (sum=0, teams=[FR-ADM (4)])
                [SE-ADM (3), NE-ADM (6)] Floor 5th (sum=0, teams=[FR-ADM (4), laurent (5)])
                    [SE-ADM (3), NE-ADM (6)] Floor 5th (sum=0, teams=[FR-ADM (4), laurent (5)])
                [laurent (5), NE-ADM (6)] Floor 5th (sum=0, teams=[FR-ADM (4), SE-ADM (3)])
                [laurent (5), SE-ADM (3)] Floor 5th (sum=0, teams=[FR-ADM (4), NE-ADM (6)])
            [FR-ADM (4), SE-ADM (3), NE-ADM (6)] Floor 5th (sum=0, teams=[laurent (5)])
            [FR-ADM (4), laurent (5), NE-ADM (6)] Floor 5th (sum=0, teams=[SE-ADM (3)])
            [FR-ADM (4), laurent (5), SE-ADM (3)] Floor 5th (sum=0, teams=[NE-ADM (6)])
    """


    def combine_floor_obj_rec(teams, floor, answers=[], p=1):
        """

        :param teams:
        :param floor: Floor
        :param answers:
        :param p:
        :return:
        """
        for team in teams:
            if floor.fit(team):
                #new branch
                combinaison = copy.deepcopy(floor)
                combinaison.append(team)
                answers.append(combinaison)

                #try to fill the rest of the branch with the rest of the teams
                reste = copy.copy(teams)
                reste.remove(team)
                combine_floor_obj_rec(reste, combinaison, answers, p+1)

    answers = []
    combine_floor_obj_rec(teams, floor, answers)

    return unique(answers)

def combine_floor2(teams, nb_places):
    answers = []

    def combine_floor_rec(teams, nb_places, answer=[]):
        for team in teams:
            team_size = TEAMS[team]
            if team_size <= nb_places and team not in answer:
                reste = (copy.copy(teams))
                reste.remove(team)
                next_answer = copy.copy(answer)
                next_answer.append(team)
                combine_floor_rec(reste, nb_places - team_size, next_answer)

        answer.sort()
        answers.append(answer)

    combine_floor_rec(teams, nb_places, [])
    print answers
    return unique(answers)


def count_floor(floor):
    c = 0
    for team in floor:
        c = c + TEAMS[team]
    return c




Combinaisons = []
teams = []
floors = []
for t in TEAMS.iteritems():
    teams.append(Team(t[0], t[1]))

for f in FLOORS.iteritems():
    floors.append(Floor(f[0], f[1]))

print teams
print floors


def compute_teams_not_used(floor, team_list):
    tmp_teams_not_used = copy.copy(team_list)
    for ateam in floor.teams:
        tmp_teams_not_used.remove(ateam)
    return tmp_teams_not_used


for combi_1st in combine_floor_obj(teams, floors[0]):
    print "-->",combi_1st
    teams_not_used = compute_teams_not_used(combi_1st, teams)
    for combi_2nd in combine_floor_obj(teams_not_used, floors[1]):
        teams_not_used2 = compute_teams_not_used(combi_2nd, teams_not_used)

        for combi_3rd in combine_floor_obj(teams_not_used2, floors[2]):
            teams_not_used3 = compute_teams_not_used(combi_3rd, teams_not_used2)

            for combi_5th in combine_floor_obj(teams_not_used3, floors[3]):
                teams_not_used4 = compute_teams_not_used(combi_5th, teams_not_used3)

                if len(teams_not_used4) == 0:
                    Combinaisons.append([combi_1st, combi_2nd, combi_3rd, combi_5th])

print "NEW"
print len(Combinaisons)
satisfied = []
for c in Combinaisons:
    if not check_team_in_floor('TREX', c[0]) \
            and not check_team_in_floor('DESTI-FULL_OFFER-QUALIF-DATA', c[0]):
        satisfied.append(c)

print len(satisfied)
for c in satisfied:
    for fl in c:
        print fl
    print "---------------"
