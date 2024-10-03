'''
It were the days of domination from the traditional metros in the team selections and everytime the team is announced for the Indian Squad, mere disappointment was left with this small town player. Dhoni’ill fate continued even during the team selections for the India A squad to tour to Zimbabwe.3 new players from Mumbai were on the list for the Indian team and it was claimed by the selectors that Dhoni was a bit younger than the 3 selected players.
  Assume the 3 players are Named X,Y and Z. The ages of the players X and Y are the same and the age of the Z is 10 more than other 2 players. Given the total age of the 3 players, find the age of the 3 players.
Input format:
First line of the input is an integer that corresponds to the total age of the 3 players.
Output format:
Output should display the ages of the three players in 3 lines. The age of the eldest player should be displayed in the last line.
'''
def main():
    total_age = int(input())
    a = (total_age - 10) / 3  # Age of players X and Y
    z = a + 10  # Age of player Z
    print(int(a))  # Age of player X
    print(int(a))  # Age of player Y
    print(int(z))  # Age of player Z (eldest)
if __name__ == "__main__":
    main()
16
16
26


program:
total_age = int(input())
a = (total_age - 10) // 3  
z = a + 10  # Age of player Z
print(a)  
print(a)  
print(z)  
