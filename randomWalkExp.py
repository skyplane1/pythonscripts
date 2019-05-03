# how likely it is that after 100 die throws step no 60 will be reached
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
all_walks = []
for i in range(500):
    random_walk = [0]

    for j in range(100): #inner loop, runs for a 100 times, before going out.This loop runs 100 times, 500 times, because of the outer loop
        step = random_walk[-1] #On each iteration step should be previous step
        dice = np.random.randint(1, 7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)

        if np.random.rand() <= 0.001:
            step = 0

        random_walk.append(step)

    all_walks.append(random_walk)

np_all_walks = np.transpose(np.array(all_walks))
ends = np_all_walks[-1]

plt.hist(ends)
plt.show()


