import sys


class Player:
    def __init__(self, name, team, matches):
        self.name = name
        self.team = team
        self.matches_played = matches

    def display_info(self):
        print("Name\t\t-\t", self.name)
        print("Team\t\t-\t", self.team)
        print("Matches Played\t-\t", self.matches_played)


class Batsman(Player):
    def __init__(self, name, team, matches, runs, balls):
        Player.__init__(self, name, team, matches)
        self.runs_scored = runs
        self.balls_faced = balls

    def calculate_strike_rate(self):
        if self.balls_faced == 0:
            print("\tNo Balls Faced\n\n")
            return 0
        return (self.runs_scored / self.balls_faced) * 100


class Bowler(Player):
    def __init__(self, name, team, matches, wickets, overs, runs):
        Player.__init__(self, name, team, matches)
        self.wickets_taken = wickets
        self.overs_bowled = overs
        self.runs_conceded = runs

    def calculate_economy(self):
        if self.overs_bowled == 0:
            print("\tNo Balls Bowled\n\n")
            return 0
        return self.runs_conceded / self.overs_bowled


class AllRounder(Batsman, Bowler):
    def __init__(self, name, team, matches, runs, balls, wickets, overs, runs_conceded):
        Batsman.__init__(self, name, team, matches, runs, balls)
        self.wickets_taken = wickets
        self.overs_bowled = overs
        self.runs_conceded = runs_conceded


class Team:
    def __init__(self):
        self.players = []

    def add_player(self):
        name = input("Enter Player Name\t-\t")
        if(name.strip().lower() == 'exit'):
            print("\n\t***Exiting Program***\n\n")
            sys.exit(1)
        team = input("Enter Team Name\t-\t")
        if(team.strip().lower() == 'exit'):
            print("\n\t***Exiting Program***\n\n")
            sys.exit(1)
        matches = input("Enter Matches Played\t-\t")        
        if(matches.strip().lower() == 'exit'):
            print("\n\t***Exiting Program***\n\n")
            sys.exit(1)
        try:
            matches = int(matches)
        except:
            print("\tInvalid Input\n\n")
            self.add_player()
        print("1 - Batsman")
        print("2 - Bowler")
        print("3 - All-Rounder")
        ch = input("Enter Player Type\t-\t")
        if(ch == '1'):
            runs = input("Enter Runs Scored\t-\t")
            if(runs.strip().lower() == 'exit'):
                print("\n\t***Exiting Program***\n\n")
                sys.exit(1)
            try:
                runs = int(runs)
            except:
                print("\tInvalid Input\n\n")
                self.add_player()
            balls = int(input("Enter Balls Faced\t-\t"))
            if(balls.strip().lower() == 'exit'):
                print("\n\t***Exiting Program***\n\n")
                sys.exit(1)
            try:
                balls = int(balls)
            except:
                print("\tInvalid Input\n\n")
                self.add_player()
            p = Batsman(name, team, matches, runs, balls)
        elif(ch == '2'):
            wickets = input("Enter Wickets Taken\t-\t")
            if(wickets.strip().lower() == 'exit'):
                print("\n\t***Exiting Program***\n\n")
                sys.exit(1)
            try:
                wickets = int(wickets)
            except:
                print("\tInvalid Input\n\n")
                self.add_player()
            overs = input("Enter Overs Bowled\t-\t")
            if(overs.strip().lower() == 'exit'):
                print("\n\t***Exiting Program***\n\n")
                sys.exit(1)
            try:
                overs = float(overs)
            except:
                print("\tInvalid Input\n\n")
                self.add_player()
            runs = input("Enter Runs Conceded\t-\t")
            if(runs.strip().lower() == 'exit'):
                print("\n\t***Exiting Program***\n\n")
                sys.exit(1)
            try:
                runs = int(runs)
            except:
                print("\tInvalid Input\n\n")
                self.add_player()
            p = Bowler(name, team, matches, wickets, overs, runs)
        elif(ch == '3'):
            runs = input("Enter Runs Scored\t-\t")
            if(runs.strip().lower() == 'exit'):
                print("\n\t***Exiting Program***\n\n")
                sys.exit(1)
            try:
                runs = int(runs)
            except:
                print("\tInvalid Input\n\n")
                self.add_player()
            balls = input("Enter Balls Faced\t-\t")
            if(balls.strip().lower() == 'exit'):
                print("\n\t***Exiting Program***\n\n")
                sys.exit(1)
            try:
                balls = int(balls)
            except:
                print("\tInvalid Input\n\n")
                self.add_player()
            wickets = input("Enter Wickets Taken\t-\t")
            if(wickets.strip().lower() == 'exit'):
                print("\n\t***Exiting Program***\n\n")
                sys.exit(1)
            try:
                wickets = int(wickets)
            except:
                print("\tInvalid Input\n\n")
                self.add_player()
            overs = input("Enter Overs Bowled\t-\t")
            if(overs.strip().lower() == 'exit'):
                print("\n\t***Exiting Program***\n\n")
                sys.exit(1)
            try:
                overs = float(overs)
            except:
                print("\tInvalid Input\n\n")
                self.add_player()
            runs_conceded = input("Enter Runs Conceded\t-\t")
            if(runs_conceded.strip().lower() == 'exit'):
                print("\n\t***Exiting Program***\n\n")
                sys.exit(1)
            try:
                runs_conceded = int(runs_conceded)
            except:
                print("\tInvalid Input\n\n")
                self.add_player()
            p = AllRounder(name, team, matches, runs, balls, wickets, overs, runs_conceded)
        elif(ch.strip().lower() == 'exit'):
            print("\n\t***Exiting Program***\n\n")
            sys.exit(1)
        else:
            print("\tInvalid Choice\n")
            return
        self.players.append(p)
        print("\tPlayer Added Successfully\n")

    def show_players(self):
        if len(self.players) == 0:
            print("\tNo Players Available\n")
            return
        for p in self.players:
            print("-----------------------")
            p.display_info()
            if isinstance(p, Batsman):
                print("Runs\t\t-\t", p.runs_scored)
                print("Strike Rate\t-\t", round(p.calculate_strike_rate(), 2))
            if isinstance(p, Bowler):
                print("Wickets\t\t-\t", p.wickets_taken)
                print("Economy\t\t-\t", round(p.calculate_economy(), 2))

    def top_batsman(self):
        batsmen = [p for p in self.players if isinstance(p, Batsman)]
        if len(batsmen) == 0:
            print("\tNo Batsmen Available\n")
            return
        top = batsmen[0]
        for b in batsmen:
            if b.calculate_strike_rate() > top.calculate_strike_rate():
                top = b
        print("\nTop Batsman\t-\t")
        top.display_info()
        print("Strike Rate\t-\t", round(top.calculate_strike_rate(), 2))

    def top_bowler(self):
        bowlers = [p for p in self.players if isinstance(p, Bowler)]
        if len(bowlers) == 0:
            print("\tNo Bowlers Available\n")
            return
        top = bowlers[0]
        for b in bowlers:
            if b.calculate_economy() < top.calculate_economy():
                top = b
        print("\nTop Bowler\t-\n")
        top.display_info()
        print("Economy\t-\t", round(top.calculate_economy(), 2))


# ---------------- MAIN MENU ---------------- #

T = Team()
while True:
    print("\n1 - Add Player")
    print("2 - Show All Players")
    print("3 - Top Batsman")
    print("4 - Top Bowler")
    print("exit - Exit Program")

    ch = input("Enter Choice\t-\t")

    if(ch == '1'):
        T.add_player()
    elif(ch == '2'):
        T.show_players()
    elif(ch == '3'):
        T.top_batsman()
    elif(ch == '4'):
        T.top_bowler()
    elif(ch.strip().lower() == 'exit'):
        print("\n\t***Exiting Program***\n")
        break
    else:
        print("\tInvalid Choice\n")