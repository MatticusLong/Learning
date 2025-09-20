# Example of a dictionary representing a football player's stats
#program is used to store and display stats for a football player using a dictionary

Tyreek_Hill = {'name': 'Tyreek Hill', 'position': 'Wide Receiver', 'jersey_number': 10, 'yards_gained': 150, 'touchdowns': 2}
Patrick_Mahomes = {'name': 'Patrick Mahomes', 'position': 'Quarterback', 'jersey_number': 15, 'yards_passed': 300, 'touchdowns': 3}
Travis_Kelce = {'name': 'Travis Kelce', 'position': 'Tight End', 'jersey_number': 87, 'yards_gained': 120, 'touchdowns': 1}

# add 25 yards to Tyreek's yards_gained
Tyreek_Hill['yards_gained'] += 25

# set a stat to a specific value
Patrick_Mahomes['touchdowns'] = 4

# add receptions even if the key doesn't exist yet
Tyreek_Hill['receptions'] = Tyreek_Hill.get('receptions', 0) + 3


#to print all stats of a player
players = [Tyreek_Hill, Patrick_Mahomes, Travis_Kelce]

for p in players:
    print(f"{p['name']} — {p['position']} #{p['jersey_number']}")
    print(f"  Yards: {p.get('yards_gained', p.get('yards_passed', 0))}  TDs: {p.get('touchdowns', 0)}")
    print()
    