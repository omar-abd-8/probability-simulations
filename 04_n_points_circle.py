import numpy as np

fits=0
experiments = 100000
n = int(input("How many points on the circle? : "))

for i in range(experiments):
    points = np.random.uniform(0, 2*np.pi, n)
    sorted_points = np.sort(points)
    gaps = np.diff(sorted_points)
    wrap_around = 2*np.pi-max(sorted_points)+min(sorted_points)
    if max(np.append(gaps, wrap_around))>=np.pi:
        fits+=1

print(f"P(All lie on a semicircle): {fits/100000:.1%}")