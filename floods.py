'''
Tamilnadu was battling one if it’s worst floods in a century last December, as several part of the state have been submerged and cut off from essential supplies. It was heartening that the Cricketers came forward to contribute for the cause of floods and it was decided amongst the team that the senior players donate 50% of their salary and junior players to donate 40% against the flood relief measures
Assume there are 6 senior players and 5 junior players. The salary of senior players Rs.X and that of junior players is Rs.Y. Find the total contribution from the cricket team towards the floods.
Input format:
First line of the input is an integer “X” that specifies the salary of the senior players in rupees.
Second line is an integer “Y” that specifies the salary of the junior players in rupees.
Output format:
Output should display a flood that gives the total contribution of money in rupees from the cricket team. The float value should be displayed correct to 2 decimal places.
'''
380000.00


program:
X = int(input())
Y = int(input())
t1 = X * 0.50 * 6  # Contribution from senior players (6 players)
t2 = Y * 0.40 * 5   # Contribution from junior players (5 players)
t = t1 + t2
print("%.2f" % t)
