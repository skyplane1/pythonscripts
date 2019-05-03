#Script to predict distribution of getting to 60 steps in  a 100 dice throws
#if dice rolls 1 or 2 => -1 step
#if dice rolls 2,3,4,5 => +1 step
#if dice rolls 6 => steps = no that occurs on next dice throw
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
all_walks = []
for i in range (100):
    step_list = [0]
    for i in range(100):
        step = step_list[-1]
        dice = np.random.randint(1,7)
        if dice <= 2 :
            step = max(0, step - 1)
        elif dice <= 5 :
            step = step + 1
        else :
            step = step + np.random.randint(1,7)

        step_list.append(step)
    all_walks.append(step_list)
print(all_walks)

np_step = np.array(all_walks)
np_aw_t = np.transpose(np_step)

plt.plot(np_aw_t)

ends = np_aw_t[-1]

plt.hist(ends)
