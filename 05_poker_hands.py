import numpy as np

experiments = 1000000
deck = np.repeat(np.arange(1, 14), 4)
four_of_a_kind=0
full_house=0
two_pairs=0

for i in range(experiments):
    cards = np.random.choice(deck, size=5, replace=False)
    values, counts = np.unique(cards, return_counts=True)
    if 4 in counts:
        four_of_a_kind+=1
    if sum(counts == 2)==2:
        two_pairs+=1
    if sum(counts == 3)==1 and sum(counts == 2)==1:
        full_house+=1

print(f"Four of a kind: {four_of_a_kind/experiments:.4%}")
print(f"Full house: {full_house/experiments:.4%}")
print(f"Two pairs: {two_pairs/experiments:.4%}")