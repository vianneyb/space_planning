import copy

alist = [{'A': 1}, {'B': 1}, {'C': 1}, {'D': 1}, {'E': 1}, {'F':1}, {'G':1}, {'H':1}, {'I':1}, {'J':1}, {'K':1}, {'L':1}, {'M':1}, {'N':1}, {'O':1}, {'P':1}, {'Q':1}, {'R':1}, {'S':1}, {'T':1}, {'U':1}, {'V':1}, {'W':1}]#, {'X':1}, ]  # 'Y','Z']


def combinaisons_while(alist):
    def subtree(tete, reste2, answers):
        if len(reste2) <= 0:
            return
        subreste = copy.copy(reste2)
        el = subreste.pop()
        next_tete = copy.copy(tete)
        next_tete.append(el)
        answers.append(next_tete)
        while len(subreste):
            subtree(next_tete, subreste, answers)
            subreste.pop()

    reste = copy.copy(alist)
    answers = []
    while len(alist):
        el = alist.pop()
        answers.append([el])
        reste.pop()
        subtree(el, reste, answers)
    return answers


def combinaisons(alist):
    def subtree(tete, teams, answers):
        for k in range(len(teams)):
            answer = copy.copy(tete)
            answer.append(teams[k])
            answers.append(answer)
            reste = teams[k+1:]
            if len(reste):
                subtree(answer, reste, answers)

    reste = copy.copy(alist)
    answers = []
    for k, el in enumerate(alist):
        answers.append([el])
        subtree([el], alist[k+1:], answers)
    return answers

comb = combinaisons(alist)

print len(comb)
# for c in comb:
#    print c
