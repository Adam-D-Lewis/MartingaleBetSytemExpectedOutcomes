import random
import numpy as np
import matplotlib.pyplot as plt

num_sets = int(1E8)
all_sets_total = 0
b_max = 500

b0 = 481
f = 1.01
max_games = np.int(np.log(b_max/b0)/np.log(f))+1

set_outcome_results = np.empty(num_sets)
num_games_in_set = np.empty(num_sets)
for i in range(num_sets):
    win = False
    set_results = 0
    set_game_num = 0

    while win is False and set_game_num < max_games:
        set_game_num += 1
        if random.uniform(0, 1) <= 0.48:
            #win
            win = True
            set_results += b0*f**(set_game_num-1)
        else:
            #loss
            set_results -= b0*f**(set_game_num-1)
    set_outcome_results[i] = set_results
    num_games_in_set[i] = set_game_num

plt.figure()
plt.plot(set_outcome_results)
plt.xlabel("set #")
plt.ylabel("outcome ($)")
plt.title("Ave. Outcome = ${0:.02f}".format(np.mean(set_outcome_results)))

print(np.mean(num_games_in_set))
plt.show()

print('bye')


