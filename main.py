import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

pW = 0.48
pL = 1-pW
b_max = 500 #max bet ($)

def total_losses(b0, f, num_losses):
    sum=0
    for i in range(0, num_losses):
        sum += f**i
    return b0*sum

def net_winnings(b0, f, num_games):
    # assumes you won on the last game and lost on all games prior
    return b0*f**(num_games-1)-total_losses(b0, f, num_games-1)


def expected_outcome(b0, f, printN=False):
    # print(b0)
    # print(f)
    N = np.int(np.log(b_max/b0)/np.log(f))+1
    if printN:
        print("N is {}".format(N))
    sum = 0
    for i in range(1, N+1):
        sum += pL**(i-1)*net_winnings(b0, f, i)

    expectation = pW*sum - pL**N*total_losses(b0, f, N)
    return expectation

# b0 = 481.00
# f = 1.01
# print(expected_outcome(b0, f, 0))

b0 = np.arange(1, 500, 1)  # initial bets
f = np.arange(1.01, 5, 0.1)  # bet increase factor (=2 in typical Martingale System)
b0, f = np.meshgrid(b0, f)

results=[]
for b0i, fi in zip(b0.flatten(), f.flatten()):
    # print("Expected outcome for b0 = {0}, f ={1:.2f} is {2}".format(b0i, fi, expected_outcome(b0i, fi)))
    results.append(expected_outcome(b0i, fi))

results = np.asarray(results)
i_opt = np.argmax(results)
b_opt = b0.flatten()[i_opt]
f_opt = f.flatten()[i_opt]
result_opt = results[i_opt]

results=np.reshape(results, b0.shape)

for var in ['b_opt', 'f_opt', 'result_opt']:
    print("{0} = {1:.04f}".format(var, eval(var)))

#plot
fig = plt.figure()
ax = fig.gca(projection='3d')

# Plot the surface.
surf = ax.plot_surface(b0, f, results, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_xlabel('Initial Bet ($)')
ax.set_ylabel('Bet Increase Factor')
ax.set_zlabel('Expected Outcome ($)')
# ax.set_zlim(0, ax.get_zlim()[1])
fig.suptitle('Expected Outcome Surface using Martingale System on Roulette')
plt.title('Min/Max Bet: \$1/\$500', fontsize=10)

plt.show()

print('bye')
