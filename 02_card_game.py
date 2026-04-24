import numpy as np

experiments=10000
my_wins=0
d_wins=0
ties=0
deck = np.repeat(np.arange(1, 14), 4)

for i in range(experiments):
    cards = np.random.choice(deck, size=2, replace=False)
    if cards[0]>cards[1]:
        my_wins+=1
    elif cards[0]<cards[1]:
        d_wins+=1
    else :
        ties+=1
print(f"My wins: {my_wins/experiments:.1%}")
print(f"Dealer wins: {d_wins/experiments:.1%}")
print(f"Ties: {ties/experiments:.1%}")
