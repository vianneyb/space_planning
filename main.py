TEAMS = {
    "FR-ADM": 11,
    "SE-ADM": 10,
    "NE-ADM": 8,
    "UK-ADM": 4,
    "CC": 14,
    "DESTI": 9,
    "CRM": 7,
    "OFFER": 7,
    "FR-OF": 4,
    "NE-OF": 2,
    "UK-OF": 2,
    "SE-OF": 4,
    "QUALIF": 4,
    "DATA": 14,
    "HP": 8,
    "TREX": 12,
    "TEA": 12,
    "TIPI": 11,
    "LAC": 10,
    "NUMBERS": 8,
    "INTERNAL": 4,
    "BRAND": 9,
    "INSPI": 8,
    "NE-MARKET": 11,
    "SE-MARKET": 8,
    "UK-MARKET": 4,
    "FR-MARKET": 8,
    "AKI": 9,
}

# arthur vianney nas daniele laurent samy carlos dana


FLOORS = {
    "1st": 52,
    "2nd": 56,
    "3rd": 68,
    "5th": 56,  # +1bench
}

import copy


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
        answer_size = TEAMS[team]
        answer = [team]
        for team in teams:
            size = TEAMS[team]
            if answer_size + size <= nb_places and team not in answer:
                answer.append(team)
                answer_size += size
        answer.sort()
        answers.append(answer)
    return unique(answers)


def count_floor(floor):
    c = 0
    for team in floor:
        c = c + TEAMS[team]
    return c


Combinaisons = []
teams = TEAMS.keys()
for combi_1st in combine_floor(teams, FLOORS['1st']):
    reste1 = copy.copy(teams)
    for el in combi_1st:
        reste1.remove(el)
    if len(reste1) == 0:
        Combinaisons.append([combi_1st, [], [], []])
    for combi_2nd in combine_floor(reste1, FLOORS['2nd']):
        reste2 = copy.copy(reste1)
        for el in combi_2nd:
            reste2.remove(el)
        if len(reste2) == 0:
            Combinaisons.append([combi_1st, combi_2nd, [], []])
        for combi_3rd in combine_floor(reste2, FLOORS['3rd']):
            reste3 = copy.copy(reste2)
            for el in combi_3rd:
                reste3.remove(el)
            if len(reste3) == 0:
                Combinaisons.append([combi_1st, combi_2nd, combi_3rd, []])
            for combi_5th in combine_floor(reste3, FLOORS['5th']):
                reste = copy.copy(reste3)
                for el in combi_5th:
                    reste.remove(el)
                    if len(reste) == 0:
                        Combinaisons.append([combi_1st, combi_2nd, combi_3rd, combi_5th])

print len(Combinaisons)
satisfied = []
for c in Combinaisons:

    if check_teams_same_floor('TEA', 'TREX', c) \
        and check_teams_same_floor('TEA', 'NUMBERS', c):
        satisfied.append(c)

print len(satisfied)
for c in satisfied:
    print c
