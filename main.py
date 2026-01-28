def play_innings(team_name, max_overs, max_wickets, target=None):
    print(f"\n--- {team_name} Innings ---")

    runs = 0
    wickets = 0
    balls = 0

    max_balls = max_overs * 6

    while balls < max_balls and wickets < max_wickets:
        # Stop if chasing team reaches target
        if target is not None and runs >= target:
            break

        ball = input("Enter ball (0-6, wd, nb, w): ").lower()

        if ball == "wd":
            runs += 1
            print("Wide! +1 run")

        elif ball == "nb":
            runs += 1
            print("No-ball! +1 run")

        elif ball == "w":
            wickets += 1
            balls += 1
            print("Wicket!")

        elif ball.isdigit() and 0 <= int(ball) <= 6:
            runs += int(ball)
            balls += 1

        else:
            print("Invalid input. Try again.")
            continue

        overs = balls // 6
        balls_in_over = balls % 6
        print(f"Score: {runs}/{wickets}  Overs: {overs}.{balls_in_over}")

    print(f"\n{team_name} Final Score: {runs}/{wickets}")
    return runs


# -------- MAIN PROGRAM --------

print("🏏 Cricket Scoring Program 🏏")

team1 = input("Enter Team 1 name: ")
team2 = input("Enter Team 2 name: ")

overs = int(input("Enter total overs: "))
wickets = int(input("Enter total wickets: "))

# Team 1 innings
team1_score = play_innings(team1, overs, wickets)

target = team1_score + 1
print(f"\nTarget for {team2}: {target}")

# Team 2 innings
team2_score = play_innings(team2, overs, wickets, target)

# -------- RESULT --------
print("\n--- Match Result ---")

if team2_score >= target:
    print(f"{team2} won the match!")
elif team2_score < team1_score:
    print(f"{team1} won the match!")
else:
    print("Match Tied!")
