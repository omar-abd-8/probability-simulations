import numpy as np

n = 100
games = 100000

# flip all coins for all games at once (matrix of 0s and 1s)
a_flips = np.random.randint(0, 2, size=(games, n + 1))
b_flips = np.random.randint(0, 2, size=(games, n))

# sum each row to get heads per game
a_heads = a_flips.sum(axis=1)
b_heads = b_flips.sum(axis=1)

# count outcomes
a_wins = (a_heads > b_heads).sum()
ties = (a_heads == b_heads).sum()
b_wins = (a_heads < b_heads).sum()

print(f"A wins: {a_wins/games:.1%}")
print(f"Ties:   {ties/games:.1%}")
print(f"B wins: {b_wins/games:.1%}")
