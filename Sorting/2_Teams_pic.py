"""
Given 2 teams' players' heights in arrays, find if you can take a pic of the
2 teams in 2 rows. All members in a row must belong to the same team


"""
def is_pic_possible(team1, team2):
    team1.sort()
    team2.sort()

    shorter = team1
    taller = team2

    if team1[0] > team2[0]:
        shorter = team2
        taller = team1

    for i in range(len(team1)):
        if shorter[i] > taller[i]:
            return False

    return True