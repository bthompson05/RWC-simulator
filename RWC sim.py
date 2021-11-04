from abc import abstractproperty
import random
import itertools

groups = {"A": {}, "B": {}, "C": {}, "D": {}}
teams = {"Ireland": {"Ranking": 1, "RankPoints": 89.47},
         "Japan": {"Ranking": 10, "RankPoints": 76.70},
         "Russia": {"Ranking": 20, "RankPoints": 64.81},
         "Samoa": {"Ranking": 16, "RankPoints": 69.08},
         "Scotland": {"Ranking": 7, "RankPoints": 81.00},
         "Canada": {"Ranking": 22, "RankPoints": 61.12},
         "Italy": {"Ranking": 14, "RankPoints": 72.04},
         "Namibia": {"Ranking": 23, "RankPoints": 61.01},
         "New Zealand": {"Ranking": 2, "RankPoints": 89.40},
         "South Africa": {"Ranking": 4, "RankPoints": 87.34},
         "Argentina": {"Ranking": 11, "RankPoints": 76.29},
         "England": {"Ranking": 3, "RankPoints": 88.13},
         "France": {"Ranking": 8, "RankPoints": 79.72},
         "Tonga": {"Ranking": 15, "RankPoints": 71.04},
         "USA": {"Ranking": 13, "RankPoints": 72.18},
         "Australia": {"Ranking": 6, "RankPoints": 84.05},
         "Fiji": {"Ranking": 9, "RankPoints": 77.43},
         "Georgia": {"Ranking": 12, "RankPoints": 73.29},
         "Uruguay": {"Ranking": 19, "RankPoints": 65.18},
         "Wales": {"Ranking": 5, "RankPoints": 87.32}}
groups_teams = {"A": [], "B": [], "C": [], "D": []}


def seeds():
    global teams
    # Creating the lists to assign the teams to
    first_seed = []
    second_seed = []
    third_seed = []
    # Loops through the dictionary, targeting the data (value)
    for team, data in teams.items():
        if data["Ranking"] < 5:
            first_seed.append(team)
        elif data["Ranking"] < 9:
            second_seed.append(team)
        else:
            third_seed.append(team)
    # Passes the seeds into the grouping function to determine groups
    grouping(first_seed, second_seed, third_seed)


def grouping(first, second, third):
    global groups
    group_1 = []
    group_2 = []
    group_3 = []
    group_4 = []

    global groups_teams
    for grp in "ABCD":
        team_seed_1 = random.choice(first)
        groups[grp][team_seed_1] = {"Played": 0, "Won": 0, "Lost": 0, "Drawn": 0, "Scored": 0,
                                    "Against": 0, "Points": 0}
        groups_teams[grp].append(team_seed_1)
        first.remove(team_seed_1)

        team_seed_2 = random.choice(second)
        groups[grp][team_seed_2] = {"Played": 0, "Won": 0, "Lost": 0, "Drawn": 0, "Scored": 0,
                                    "Against": 0, "Points": 0}
        groups_teams[grp].append(team_seed_2)
        second.remove(team_seed_2)

        team_seed_3 = random.choice(third)
        groups[grp][team_seed_3] = {"Played": 0, "Won": 0, "Lost": 0, "Drawn": 0, "Scored": 0,
                                    "Against": 0, "Points": 0}
        groups_teams[grp].append(team_seed_3)
        third.remove(team_seed_3)

        team_seed_4 = random.choice(third)
        groups[grp][team_seed_4] = {"Played": 0, "Won": 0, "Lost": 0, "Drawn": 0, "Scored": 0,
                                    "Against": 0, "Points": 0}
        groups_teams[grp].append(team_seed_4)
        third.remove(team_seed_4)

        team_seed_5 = random.choice(third)
        groups[grp][team_seed_5] = {"Played": 0, "Won": 0, "Lost": 0, "Drawn": 0, "Scored": 0,
                                    "Against": 0, "Points": 0}
        groups_teams[grp].append(team_seed_5)
        third.remove(team_seed_5)


def matches(team_1, team_2, group, stage):
    global teams
    global groups
    # Assigning each teams rank points
    team_1_rank_points = teams[team_1]["RankPoints"]
    team_2_rank_points = teams[team_2]["RankPoints"]
    team_1_score = 1
    team_2_score = 1
    # Generating random team scores based on their ranking points
    while team_1_score == 1 or team_1_score == 2 or team_1_score == 4:
        team_1_score = random.randint(0, round(int(team_1_rank_points)) // 2)
    while team_2_score == 1 or team_2_score == 2 or team_2_score == 4:
        team_2_score = random.randint(0, round(int(team_2_rank_points)) // 2)
    # Determining random winner if first round ends in draw
    if stage == "knockout":
        if team_1_score == team_2_score:
            team_win_xt = random.choice(["team_1", "team_2"])
            if team_win_xt == "team1":
                team_1_score += 3
                print(team_1, team_1_score, "-", team_2_score, team_2, "AET")
                return team_1
            if team_win_xt == "team_2":
                team_1_score += 3
                print(team_1, team_1_score, "-", team_2_score, team_2, "AET")
                return team_2
        else:
            print(team_1, team_1_score, "-", team_2_score, team_2)
            if team_1_score > team_2_score:
                return team_1
            else:
                return team_2
    else:
        print(team_1, team_1_score, "-", team_2_score, team_2)
        groups[group][team_1]["Played"] += 1
        groups[group][team_1]["Scored"] += team_1_score
        groups[group][team_1]["Against"] += team_2_score
        groups[group][team_2]["Played"] += 1
        groups[group][team_2]["Scored"] += team_2_score
        groups[group][team_2]["Against"] += team_1_score
        if team_1_score > team_2_score:
            groups[group][team_1]["Won"] += 1
            groups[group][team_2]["Lost"] += 1
            groups[group][team_1]["Points"] += 4
        elif team_2_score > team_1_score:
            groups[group][team_2]["Won"] += 1
            groups[group][team_1]["Lost"] += 1
            groups[group][team_2]["Points"] += 4
        else:
            groups[group][team_1]["Points"] += 2
            groups[group][team_1]["Points"] += 4

    rank_point_adjustment(team_1, team_2, team_1_score, team_2_score)


def rank_point_adjustment(team_1, team_2, team_1_score, team_2_score):
    global teams
    team_1_rank = teams[team_1]["Ranking"]
    team_2_rank = teams[team_2]["Ranking"]
    points_exchange = abs(team_1_score - team_2_score)
    if team_1_score > team_2_score:
        teams[team_1]["RankPoints"] += round(2 * (points_exchange / 100))
        teams[team_2]["RankPoints"] -= round(2 * (points_exchange / 100))
    if team_2_score > team_1_score:
        teams[team_2]["RankPoints"] += round(4 * (points_exchange / 100))
        teams[team_1]["RankPoints"] -= round(4 * (points_exchange / 100))


def match_generation():
    global groups_teams
    group_a = groups_teams.get('A')
    group_b = groups_teams.get('B')
    group_c = groups_teams.get('C')
    group_d = groups_teams.get('D')
    fixtures_a = []
    fixtures_b = []
    fixtures_c = []
    fixtures_d = []
    print("The results from fixtures in Group A are:\n")
    for i in range(0, len(group_a) + 1):
        for subset in itertools.combinations(group_a, i):
            if len(subset) == 2 and subset not in fixtures_a:
                fixtures_a.append(subset)
                teams = str(subset)
                teams = teams.replace("(", "").replace(")", "").replace("'", "")
                teams_split = teams.split(',')
                first_team = teams_split[0]
                second_team = teams_split[1]
                second_team = second_team.lstrip()
                matches(first_team, second_team, "A", "groupstage")

    print("The results from fixtures in Group B are:\n")
    for i in range(0, len(group_b) + 1):
        for subset in itertools.combinations(group_b, i):
            if len(subset) == 2 and subset not in fixtures_b:
                fixtures_b.append(subset)
                teams = str(subset)
                teams = teams.replace("(", "").replace(")", "").replace("'", "")
                teams_split = teams.split(',')
                first_team = teams_split[0]
                second_team = teams_split[1]
                second_team = second_team.lstrip()
                matches(first_team, second_team, "B", "groupstage")

    print("The results from fixtures in Group C are:\n")
    for i in range(0, len(group_c) + 1):
        for subset in itertools.combinations(group_c, i):
            if len(subset) == 2 and subset not in fixtures_c:
                fixtures_c.append(subset)
                teams = str(subset)
                teams = teams.replace("(", "").replace(")", "").replace("'", "")
                teams_split = teams.split(',')
                first_team = teams_split[0]
                second_team = teams_split[1]
                second_team = second_team.lstrip()
                matches(first_team, second_team, "C", "groupstage")

    print("The results from fixtures in Group D are:\n")
    for i in range(0, len(group_d) + 1):
        for subset in itertools.combinations(group_d, i):
            if len(subset) == 2 and subset not in fixtures_d:
                fixtures_d.append(subset)
                teams = str(subset)
                teams = teams.replace("(", "").replace(")", "").replace("'", "")
                teams_split = teams.split(',')
                first_team = teams_split[0]
                second_team = teams_split[1]
                second_team = second_team.lstrip()
                matches(first_team, second_team, "D", "groupstage")


def knockout_stages_teams():
    global groups
    global groups_teams
    group_a, group_b, group_c, group_d = groups_teams.get('A'), groups_teams.get('B'), groups_teams.get(
        'C'), groups_teams.get('D')
    group_a_points, group_b_points, group_c_points, group_d_points = {}, {}, {}, {}
    for i in group_a:
        points = groups["A"][i].get("Points")
        gd = groups["A"][i].get("Scored") - groups["A"][i].get("Against")
        group_a_points[i] = {"Points": points, "GD": gd}
    group_a_sorted = sorted(group_a_points.items(), key=lambda x: (x[1]['Points'], x[1]["GD"]))
    group_a_sorted.reverse()
    group_a_1, group_a_2 = (group_a_sorted[0][0]), (group_a_sorted[1][0])

    for i in group_b:
        points = groups["B"][i].get("Points")
        gd = groups["B"][i].get("Scored") - groups["B"][i].get("Against")
        group_b_points[i] = {"Points": points, "GD": gd}
    group_b_sorted = sorted(group_b_points.items(), key=lambda x: (x[1]['Points'], x[1]["GD"]))
    group_b_sorted.reverse()
    group_b_1, group_b_2 = (group_b_sorted[0][0]), (group_b_sorted[1][0])

    for i in group_c:
        points = groups["C"][i].get("Points")
        gd = groups["C"][i].get("Scored") - groups["C"][i].get("Against")
        group_c_points[i] = {"Points": points, "GD": gd}
    group_c_sorted = sorted(group_c_points.items(), key=lambda x: (x[1]['Points'], x[1]["GD"]))
    group_c_sorted.reverse()
    group_c_1, group_c_2 = (group_c_sorted[0][0]), (group_c_sorted[1][0])

    for i in group_d:
        points = groups["D"][i].get("Points")
        gd = groups["D"][i].get("Scored") - groups["D"][i].get("Against")
        group_d_points[i] = {"Points": points, "GD": gd}
    group_d_sorted = sorted(group_d_points.items(), key=lambda x: (x[1]['Points'], x[1]["GD"]))
    group_d_sorted.reverse()
    group_d_1, group_d_2 = (group_d_sorted[0][0]), (group_d_sorted[1][0])


    knockout_stages(group_a_1, group_a_2, group_b_1, group_b_2, group_c_1, group_c_2, group_d_1, group_d_2)

def knockout_stages(a1, a2, b1, b2, c1, c2, d1, d2):
    print("\nThe quarter-finalists are:", a1, a2, b1, b2, c1, c2, d1, d2)
    semis = []
    qf1 = matches(a1, b2, "", "knockout")
    semis.append(qf1)
    qf2 = matches(b1, a2, "", "knockout")
    semis.append(qf2)
    qf3 = matches(c1, d2, "", "knockout")
    semis.append(qf3)
    qf4 = matches(d1, c2, "", "knockout")
    semis.append(qf4)
    print("\nThe semi-finalists are:",semis[0], semis[1], semis[2], semis[3])
    f1 = matches(semis[0], semis[1], "", "knockout")
    f2 = matches(semis[2], semis[3], "", "knockout")
    finals = [f1, f2]
    semis.remove(f1)
    semis.remove(f2)
    t1 = matches(semis[0], semis[1], "", "knockout")
    semis.remove(t1)
    t2 = semis[0]
    final_1 = matches(finals[0], finals[1], "", "knockout")
    finals.remove(final_1)
    final_2 = finals[0]
    print("In fourth place, there is {}, in third place there is {}, in second place there is {} and the winners are {}.".format(t2, t1, final_2, final_1))

seeds()
match_generation()
knockout_stages_teams()
