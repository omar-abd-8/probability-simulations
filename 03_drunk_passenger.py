import numpy as np

win = 0

for m in range(100000):
    seats = np.zeros(100, dtype=int)
    seats[np.random.randint(0, 100)] = 1
    for i in range(1,99):
        if seats[i]==0:
            seats[i]=1
        else :
            seats[np.random.choice(np.where(seats == 0)[0])]=1
    if seats[99]==0:
        win+=1

print(f"P(win): {win/100000:.1%}")
